from django.contrib import admin
from .models.categories import Categories
from .models.products import Products
from .models.admin import CustomAdmin
from .models.subcategories import SubCategories

# Registering models here.
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(CustomAdmin)
# admin.site.register(CatProducts)
admin.site.register(SubCategories)
