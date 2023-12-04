from django.contrib import admin
from .admin_models.categories import Categories
from .admin_models.products import Products
from .admin_models.admin import CustomAdmin

# Registering models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(CustomAdmin)