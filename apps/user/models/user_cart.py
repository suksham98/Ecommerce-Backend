from django.db import models
from .user import CustomUser
import uuid

# Cart Model for User

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
