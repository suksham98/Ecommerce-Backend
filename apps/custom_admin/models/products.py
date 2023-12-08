from django.db import models
from .admin import CustomAdmin
from .categories import Categories
import uuid

# Product Model
class Products(models.Model):
    
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    images = models.ImageField(upload_to='images')
    description = models.CharField(max_length=100, default='')
    material = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    instructions = models.CharField(max_length=100)
    manufacture = models.CharField(max_length=200)
    weight = models.CharField(max_length=50)
    price = models.FloatField()
    added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



