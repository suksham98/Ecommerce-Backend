from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from .manager import AdminManager

# Customized admin model
class CustomAdmin(AbstractBaseUser):
    username = None
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13, unique=True)
    user_profile_image = models.ImageField(upload_to='profile_image')
    email = models.EmailField(unique=True)

    objects = AdminManager()

    USERNAME_FIELD = "phone_number"   #USERNAME_FIELD could be single value only
    REQUIRED_FIELDS =[]