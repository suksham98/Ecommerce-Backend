from django.db import models
from ..models import CustomUser
import uuid

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser


# Customized user model
class UserCart(models.Model):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    added_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    total = models.FloatField()
    payable_amount = models.FloatField()
    status = models.IntegerField(default=1)   #0- deactive, 1 - active, 2- delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
