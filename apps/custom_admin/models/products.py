from django.db import models
from .admin import CustomAdmin
from .categories import Categories
from .subcategories import SubCategories
import uuid

# Product Model
# class Products(models.Model):
    
#     _id = models.UUIDField(
#         primary_key = True, 
#         default = uuid.uuid4, 
#         editable = False,
#         unique = True
#     )
#     category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     name = models.CharField(max_length=100)
#     images = models.ImageField(upload_to='images/', blank=True, null=True)
#     description = models.CharField(max_length=100, default='')
#     material = models.CharField(max_length=100)
#     color = models.CharField(max_length=50)
#     instructions = models.CharField(max_length=100)
#     manufacture = models.CharField(max_length=200)
#     weight = models.CharField(max_length=50)
#     price = models.FloatField()
#     added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE)
#     status = models.IntegerField(default=1)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)



class Products(models.Model):
    
    _id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False,
        unique = True
    )
    # category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    sub_category_id = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='sub_id')
    name = models.CharField(max_length=100)
    price = models.FloatField()
    unit = models.CharField(max_length=50)
    time = models.CharField(max_length=50, default='')
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    manufacturer_details = models.CharField(max_length=200)
    instructions = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, default='')
    added_by = models.ForeignKey(CustomAdmin, on_delete = models.CASCADE, related_name='prod_admin')
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




# class CatProducts(models.Model):
#     id = models.UUIDField(
#         primary_key = True, 
#         default = uuid.uuid4, 
#         editable = False,
#         unique = True
#     )
#     category = models.ForeignKey(Categories, on_delete = models.CASCADE, related_name='catid')
#     subCategory = models.ForeignKey(SubCategories, on_delete = models.CASCADE, related_name='subid')
#     productName = models.CharField(max_length=100)
#     # catogaryImage = models.ImageField(upload_to='images')
#     productImage = models.ImageField(upload_to='images')
#     quantity = models.CharField(max_length=100)
#     price = models.FloatField()
#     time = models.TimeField()
#     orderQuantity = models.IntegerField(default=0)







'''
{
    id: "60",
    time: "10 MINS",
    catogary: "Home Appliances",
    productName: "Chimney",
    catogaryImage: PRODUCT_IMAGES.HOME_APP_CATEGORY,
    productImage: PRODUCT_IMAGES.HOME_APP1,
    quantity: "3810 g",
    price: 14000,
    orderQuantity: 0,
  },'''


