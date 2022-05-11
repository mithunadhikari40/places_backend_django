import json

from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import APISettings, USER_SETTINGS, DEFAULTS, IMPORT_STRINGS
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken, BlacklistMixin, Token

from apps.user_auth.models import UserAuthModel
from apps.user_auth.serializers import UserAuthSerializer
from apps.user_auth.tokenization import get_token_for_user

from django.conf import settings


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
        request_body = json.loads(request.body)

        if 'email' not in request_body:
            return Response({'error': 'email is required'}, status=status.HTTP_400_BAD_REQUEST)
        if 'password' not in request_body:
            return Response({'error': 'password is required'}, status=status.HTTP_400_BAD_REQUEST)
        email = request_body['email']
        password = request_body['password']
        data = {}

        try:

            account = UserAuthModel.objects.get(email=email)
        except BaseException as e:
            # raise ValidationError({"error": f'{str(e)}'})
            return Response({'error': f'{str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

        token = get_token_for_user(account)
        if not check_password(password, account.password):
            return Response({'error': "Incorrect Login credentials"}, status=status.HTTP_400_BAD_REQUEST)
            # raise ValidationError({"error": "Incorrect Login credentials"})

        if account:
            if account.is_active:
                login(request, account)
                data["message"] = "Login Successful"
                serializer = self.get_serializer(account, many=False)
                data["user"] = serializer.data
                data.update(token)

                return Response(data)
            else:
                return Response({'error': 'Account is not active'}, status=status.HTTP_400_BAD_REQUEST)
                # raise ValidationError({"error": f'Account not active'})
        else:
            return Response({'error': 'Account does not exist for the provided credentials'},
                            status=status.HTTP_400_BAD_REQUEST)
            # raise ValidationError({"error": f'Account doesnt exist'})


class LogOutApi(GenericAPIView):
    serializer_class = UserAuthSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        user = request.user
        try:
            # refresh_token = request.META.get("Authorization")
            # refresh_token = request.headers.get('Authorization')
            refresh_token = request.data["refresh_token"]
            # split_part = refresh_token.split()[1].strip()
            print(f"The current user is this one {refresh_token}")

            token = RefreshToken(refresh_token)
            token.blacklist()

            # request.user.auth_token.delete()
            logout(request)
            return Response({'message': 'User Logged out successfully'})
        except BaseException as e:
            return Response({'message': f'{str(e)}'})

