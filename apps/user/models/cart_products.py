from django.db import models
from .user import CustomUser
import uuid
from ...custom_admin.models.products import Products
from .user_cart import UserCart

# Create your models here.
class CartProducts(models.Model):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    added_by = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    cart_id = models.ForeignKey(UserCart, on_delete = models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete = models.CASCADE)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.IntegerField(default=1)   #0- deactive, 1 - active, 2- deleted
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

