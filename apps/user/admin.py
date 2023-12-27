from django.contrib import admin
from .models.user import CustomUser
from .models.user_cart import UserCart
from .models.cart_products import CartProducts

class UserAdmin(admin.ModelAdmin):
    list_display = ('_id', 'username', 'first_name', 'last_name', 'phone_number', 'user_profile_image', 'user_bio', 'email')

# Register your models here.
admin.site.register(CustomUser, UserAdmin)
admin.site.register(UserCart)
admin.site.register(CartProducts)
