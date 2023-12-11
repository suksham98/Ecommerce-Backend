from django.db import models
import uuid
from ..custom_admin.models.admin import CustomAdmin
from fcm_django.models import FCMDevice
# from fcm_django.fcm import fcm_send_topic_message

# Create your models here.
class NotifyProduct(models.Model):
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.IntegerField(default=1)   #0- deactive, 1 - active, 2- delete
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    verbose_name = 'Product Notification'


class CustomFCMDevice(FCMDevice):

    device_type = models.CharField(max_length=255, blank=True, null=True)
    os_version = models.CharField(max_length=20, blank=True, null=True)
    # related_user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, null=True, blank=True)


    def custom_method(self):
        # Add custom methods if needed
        pass

    class Meta:
        # Add any additional Meta options if needed
        pass
