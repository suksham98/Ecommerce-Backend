from rest_framework import serializers
from .models.admin import CustomAdmin

class AdminSerializer(serializers.ModelSerializer): #ModelSerializer is a base class for class AdminSerializer
    class Meta:
        model = CustomAdmin
        fields = ('name','phone_number')