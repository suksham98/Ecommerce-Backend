from django.db import models
import uuid
import PIL
from django.contrib.auth.models import AbstractBaseUser
from PIL import Image
from io import BytesIO
from django.core.files import File
import os
from django_resized import ResizedImageField

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
    user_profile_image_thumbnail = models.ImageField(upload_to='images/thumbnails', blank=True, null=True)
    user_bio = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)

    # objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]

    def create_thumbnail(self):
        user_profile_image_thumbnail = Image.open(self.user_profile_image.path)

        width, height = user_profile_image_thumbnail.size
        user_profile_image_thumbnail = user_profile_image_thumbnail.resize((width, height))    #PIL.Image.ANTIALIAS)
        thumbnail_path = os.path.join(
            'images/thumbnails',
            f"{os.path.splitext(os.path.basename(self.user_profile_image.name))[0]}_thumbnail.jpg"
        )

        user_profile_image_thumbnail.save(thumbnail_path, format='JPEG')

        self.user_profile_image_thumbnail = thumbnail_path
        return thumbnail_path

        # final_image = ResizedImageField(scale=0.5, quality=75, upload_to='whatever')



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.create_thumbnail()
