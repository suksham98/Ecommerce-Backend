from django.db import models
from .admin import CustomAdmin
from .categories import Categories
import uuid

# Create your models here.

class SubCategories(models.Model):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    description = models.CharField(max_length=100, default='')
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='cat_id')
    added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE, related_name='sub_admin')
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)