from django.db import models
from .admin import CustomAdmin
import uuid

# Create your models here.

class Categories(models.Model):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, default='')
    added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)