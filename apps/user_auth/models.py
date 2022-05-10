from django.contrib.auth.models import PermissionsMixin
from django.db import models
from apps.utils.timestamp.models import TimeStamp

"""Define a custom User model that has input fields of our own choosing. There are multiple ways of doing that such 
as using AbstractUser or AbstractBaseUser modules in Django. For this project, we will be going with the 
AbstractBaseUser module."""

"""The below code first creates an Account Manager class that has all the settings needed to create a superuser and a 
regular user. """
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class AuthUserManager(BaseUserManager):
    def create_user(self, name, email, phone, password, **extra_fields):
        if not email:
            raise ValueError("Email address is Mandatory")
        if not name:
            raise ValueError("Name is Mandatory")
        if not phone:
            raise ValueError("Phone is Mandatory")
        if not password:
            raise ValueError('Password is mandatory')
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        user = self.create_user(
            email=email,
            name=f'Admin {email}',
            password=password,
            phone=1234567890,
            **extra_fields
        )
        return user


"""This class creates a User model which defines all the fields and their settings for a User."""


class UserAuthModel(AbstractBaseUser, TimeStamp,PermissionsMixin):
    name = models.CharField(null=False, blank=False, max_length=512)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone = models.FloatField(max_length=11)
    password = models.CharField(max_length=512)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    push_token = models.CharField(null=True, blank=True, max_length=1024)

    USERNAME_FIELD = 'email'
    objects = AuthUserManager()
    # active_objects = AuthUserManager()

    class Meta:
        db_table = "user_table"
        app_label = "user_auth"

    def __str__(self):
        return self.name
