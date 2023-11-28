from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Customized user model
class CustomUser(AbstractBaseUser):
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=13, unique=True)
    user_profile_image = models.ImageField(upload_to='profile_image')
    user_bio = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    # objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =['phone_number']

    # class Meta:
    #     permissions = [
    #         # Define custom permissions if needed
    #     ]

