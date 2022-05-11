from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView
# Create your views here.
from rest_framework.permissions import AllowAny
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
                account.is_active = True
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
            account = UserAuthModel.objects.get(email='')
            account.delete()
            raise ValidationError({'400': f'{str(e)}'})

        except KeyError as e:
            raise ValidationError({'400': f'{str(e)}'})


