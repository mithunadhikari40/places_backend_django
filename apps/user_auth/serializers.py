from django.contrib import admin

from .models import UserAuthModel

from .models import UserAuthModel
from rest_framework import serializers


class UserAuthSerializer(serializers.ModelSerializer):
    name = serializers.CharField(allow_blank=False, allow_null=False, max_length=512)
    email = serializers.EmailField(allow_null=False, allow_blank=False)
    phone = serializers.FloatField()
    password = serializers.CharField(max_length=512)
    # registration_date = serializers.DateTimeField(allow_null=True)
    is_superuser = serializers.BooleanField(default=False)
    is_staff = serializers.BooleanField(default=True)
    push_token = serializers.CharField(max_length=1024)

    def create(self, validated_data):
        return UserAuthModel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        instance.is_superuser = validated_data.get('is_superuser', instance.is_admin)
        instance.is_staff = validated_data.get('is_staff', instance.is_admin)
        instance.push_token = validated_data.get('push_token', instance.push_token)
        instance.save()
        return instance

    """Field level validation, Its syntax will be validate_ followed by field name
        We either raise an validation error or return that value, we can access the value in second parameter"""

    def validate_password(self, value):
        pass_len = len(value)
        if pass_len < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long.")
        return value

    """Object level validation, Its syntax will be validate. We can access all the data in the second parameter
           We either raise an validation error or return that object, we can access the object in second parameter"""

    def validate(self, data):
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        password = data.get('password')

        if name.lower() == password.lower():
            raise serializers.ValidationError("Password is too similar to name")
        if email.lower() == password.lower():
            raise serializers.ValidationError("Password is too similar to email")
        if str(phone).lower() == password.lower():
            raise serializers.ValidationError("Password is too similar to phone")
        return data

    class Meta:
        extra_kwargs = {'password': {'write_only': True}}
        model = UserAuthModel
        fields = [
            'id',
            'name',
            'email',
            'phone',
            'password',
            # 'registration_date',
            'push_token',
            'is_staff',
            'is_superuser'
        ]
