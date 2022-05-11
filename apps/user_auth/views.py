import json

from django.contrib.auth import login
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import Token

from apps.user_auth.models import UserAuthModel
from apps.user_auth.serializers import UserAuthSerializer
from apps.user_auth.tokenization import get_token_for_user


class RegisterApi(GenericAPIView):
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                account = serializer.save()
                # account.is_active = True
                account.password = make_password(account.password)
                account.save()
                # token = Token.objects.get_or_create(user=account)[0].key
                token = get_token_for_user(account)

                data = {
                    'message': 'User Created Successfully',
                    'user': {
                        'email': account.email,
                        'phone': account.phone,
                        'password': account.password,
                        'registration_date': account.registration_date,
                        'push_token': account.push_token,
                        'id': account.id,
                        'is_superuser': account.is_superuser
                    },
                    # 'token': token
                }
                data.update(token)
                return Response(data)
            else:
                print(f"The invalid set of data is {serializer.errors}")
                return Response(serializer.errors)

        except IntegrityError as e:
            # account = UserAuthModel.objects.get(email='')
            # account.delete()
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        except KeyError as e:
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)


class LoginApi(GenericAPIView):
    serializer_class = UserAuthSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = {}
        request_body = json.loads(request.body)
        email = request_body['email']
        password = request_body['password']
        try:

            account = UserAuthModel.objects.get(email=email)
        except BaseException as e:
            raise ValidationError({"error": f'{str(e)}'})

        token = get_token_for_user(account)
        if not check_password(password, account.password):
            raise ValidationError({"error": "Incorrect Login credentials"})

        if account:
            if account.is_active:
                login(request, account)
                data["message"] = "Login Successful"
                serializer = self.get_serializer(account, many=False)
                data["user"] = serializer.data
                data.update(token)

                return Response(data)
            else:
                raise ValidationError({"error": f'Account not active'})
        else:
            raise ValidationError({"error": f'Account doesnt exist'})
