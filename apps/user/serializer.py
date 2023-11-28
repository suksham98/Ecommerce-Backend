from rest_framework import serializers
from .models import CustomUser
from utils.common_functions import hash_password

class UserSerializer(serializers.ModelSerializer): #ModelSerializer is a base class for class UserSerializer
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'password')
        extra_fields = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # instance.password = hash_password(password)
            
        instance.save()
        return instance
