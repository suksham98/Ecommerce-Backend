from rest_framework import serializers
from .models import CustomAdmin

class AdminSerializer(serializers.ModelSerializer): #ModelSerializer is a base class for class UserSerializer
    class Meta:
        model = CustomAdmin
        fields = ('name','phone_number')