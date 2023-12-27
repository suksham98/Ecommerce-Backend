from django.db import models
import uuid
import PIL
from django.contrib.auth.models import AbstractBaseUser
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.core.files.storage import default_storage
import os
from django.core.files.base import ContentFile


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
    user_profile_image = models.FileField(upload_to='images/', blank=True, null=True)
    user_profile_image_thumbnail = models.FileField(upload_to='', blank=True, null=True)
    user_bio = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    # objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
