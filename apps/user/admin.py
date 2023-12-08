from django.contrib import admin
from .models.user import CustomUser
from .models.user_cart import UserCart
from .models.cart_products import CartProducts


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(UserCart)
admin.site.register(CartProducts)



