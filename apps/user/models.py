from django.db import models
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManager

# Customized user model
class CustomUser(AbstractBaseUser):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    username = None
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='')
    phone_number = models.CharField(max_length=13)
    user_profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    user_bio = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    # objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]

    # class Meta:
    #     permissions = [
    #         # Define custom permissions if needed
    #     ]

