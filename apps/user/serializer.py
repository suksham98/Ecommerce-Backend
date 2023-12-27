from rest_framework import serializers
from .models.user import CustomUser
from .models.user_cart import UserCart
from ..custom_admin.models.categories import Categories
from ..custom_admin.models.subcategories import SubCategories
from ..custom_admin.models.products import Products
from utils.common_functions import hash_password, create_thumbnail, create_thumbnail


#Serializer for user
class UserSerializer(serializers.ModelSerializer):
    user_profile_image = serializers.ImageField(write_only=True, required=False)

    def get_user_profile_image(self, obj):
        
        if obj.user_profile_image:
            return obj.user_profile_image.url
        
        
    class Meta:
        model = CustomUser
        fields = ('_id', 'first_name', 'last_name', 'email','phone_number', 'password', 'user_profile_image', 'user_profile_image_thumbnail')
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def create(self, validated_data):

        password = validated_data.pop('password', None)
        user_profile_image = validated_data.pop('user_profile_image', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
            # instance.password = hash_password(password)

        if user_profile_image is not None:
            instance.user_profile_image = user_profile_image
            instance.user_profile_image_thumbnail = f"images/thumbnails/{user_profile_image}_thumbnail.jpg"
            
            create_thumbnail(user_profile_image)

        instance.save()
        return instance
   



class CommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('__all__')

    category_id = serializers.PrimaryKeyRelatedField(queryset=Categories.objects.all())


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ('__all__')



class CommonUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['_id', 'first_name', 'last_name', 'email','phone_number', 'password', 'user_profile_image', 'user_profile_image_thumbnail']


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategories
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')


class UserCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCart
        fields = ('__all__')

