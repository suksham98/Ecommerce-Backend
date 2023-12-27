from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.db.models import Q
from ..models.user import CustomUser
from ...custom_admin.models.categories import Categories
from ...custom_admin.models.products import Products
from ...custom_admin.models.subcategories import SubCategories
from ..models.user_cart import UserCart
from ..models.cart_products import CartProducts
from ..serializer import UserSerializer, CommonSerializer, CategorySerializer, SubCategorySerializer, ProductSerializer, UserCartSerializer
from utils.common_functions import auth
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from drf_yasg.utils import swagger_auto_schema
from services.user_services.swagger import *
from django.http import HttpResponse



class CategoriesView(APIView):
    parser_classes = [FormParser]

    @swagger_auto_schema(
            operation_id='Get Categories list',
            operation_description='Get Categories or products related to specific category. ',
            manual_parameters=categories_list_user_manual_parameters + header_parameters,
            responses=categories_list_user_responses
    )
    def post(self, request):
        categories = Categories.objects.filter(status=1)

        if request.GET.get('search'):
            search = request.GET.get('search')

            categories = categories.filter(
            Q(name__icontains = search) |
            Q(_id__icontains = search)
            )
        
        data = {'categories': [], 'products': []}
        search = request.GET.get('search')
        products = Products.objects.filter()
        product_serializer = CommonSerializer(products, many=True)
        categories['products'] = product_serializer
        data['categories'].append()

        # for category in categories:
        #     products = Products.objects.filter(category_id=category._id)
        #     product_serializer = CommonSerializer(products, many=True)
            
            # data['categories'].append(CategorySerializer(category).data)
            # data['products'].extend(product_serializer.data)

        return Response(data)



class CategoryProductsListView(APIView):
    parser_classes = [FormParser]

    @swagger_auto_schema(
            operation_id='Get Categories list',
            operation_description='Get Categories or products related to specific category. ',
            manual_parameters=categories_list_user_manual_parameters + header_parameters,
            responses=categories_list_user_responses
    )
    def post(self, request):
        print("categoryyyyyyyyyyyy:", request.user)
        categories = Categories.objects.filter(status=1)

        if request.GET.get('search'):
            data = {'products': []}
            product_list = Products.objects.filter(status=1)
            search = request.GET.get('search')

            products = product_list.filter(
                Q(name__icontains=search) |
                Q(_id__icontains=search)
            )
            product_serializer = ProductSerializer(products, many=True)
            data['products'] = product_serializer.data
            return Response(data)

        data = {'categories': []}

        for category in categories:
            category_data = CategorySerializer(category).data
            sub_categories = SubCategories.objects.filter(category_id=category._id, status=1)
            
            sub_category_list = []
            
            for sub_category in sub_categories:
                sub_category_data = CommonSerializer(sub_category).data
                products = Products.objects.filter(sub_category_id=sub_category._id)
                product_serializer = ProductSerializer(products, many=True)
                sub_category_data['products'] = product_serializer.data
                
                sub_category_list.append(sub_category_data)
            
            category_data['subcategories'] = sub_category_list
            data['categories'].append(category_data)

        return Response(data)



class ProductsView(APIView):
    parser_classes = [FormParser]

    @swagger_auto_schema(
            operation_id='Get Products list',
            operation_description='Get products list or any specific product. ',
            manual_parameters=products_list_user_manual_parameters + header_parameters,
            responses=products_list_user_responses
    )
    def post(self, request):
        auth(request)
        
        products = Products.objects.filter(status=1)
        queryset = Products.objects.all()

        data = {'products': []}

        if request.GET.get('search'):
            queryset = products.filter(name__icontains = request.GET.get('search'))
        
        products_serializer = ProductSerializer(queryset, many=True)
        data['products'].append(products_serializer.data)
    
        return Response(data)



# @auth
# def products_view(self, request):
#         print("66666666666:",request.user)
#         products = Products.objects.filter(status=1)
#         queryset = Products.objects.all()

#         if request.GET.get('search'):
#             queryset = products.filter(name__icontains = request.GET.get('search'))
        
#         serializer = ProductSerializer(queryset, many=True)
    
#         return Response(serializer.data)




# class HomeView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         algorithm_used = 'HS256'
        
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
        
#         try:
#             payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
#         except jwt.ExpiredSignatureError as e:
#             raise AuthenticationFailed('Unauthenticated!') from e

#         user = CustomUser.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    


class AddEditCartView(APIView):
    parser_classes = [FormParser]

    @swagger_auto_schema(
            operation_id='Add a product into cart',
            operation_description='To Add a product into cart or modify Cart. ',
            manual_parameters=add_to_cart_manual_parameters + header_parameters,
            responses=add_to_cart_responses
    )
    def post(self, request):
        auth(request)
        user_info = request.user
        # print("000000000000000000:", request.user=='AnonymousUser')

        if request.user=='AnonymousUser':
            return HttpResponse({"error" : "User not found"})

        user_instance = get_object_or_404(CustomUser, _id=user_info['_id'])

        if cart_data := UserCart.objects.filter(added_by=user_instance).first():
            cart_serializer = UserCartSerializer(cart_data)
            extra_vals = {'cart_id': cart_serializer.data['_id']}

        else:

            data_to_add = UserCart.objects.create(
                added_by=user_instance,
                total=0,
                payable_amount=0
            )
            print(data_to_add)
            data_to_add.save()
            extra_vals = {'cart_id': data_to_add._id}
        if request.data['product_id']:
            return addProductToCart(request, user_info, extra_vals)





def addProductToCart(req, user_data, extra_values):
    
    product_details = Products.objects.filter(_id=req.data['product_id']).first()
    product_in_cart = CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['_id']).first()

    if product_details:
        if product_in_cart:
            if req.data['quantity']==0:
                CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['_id']).delete()
            elif req.data['quantity']:
                data_to_update = {}
                data_to_update.quantity = req.data['quantity']
                data_to_update.price = req.data['quantity'] * int(product_details['price'])
                CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['_id']).update(data_to_update)

        else:
            added_by_user =  get_object_or_404(CustomUser, _id=user_data['_id'])
            cart_id = get_object_or_404(UserCart, _id = extra_values['cart_id'])
            product_id = get_object_or_404(Products, _id = req.data['product_id'])
            data_to_set = CartProducts.objects.create(
                price = req.data['quantity'] * int(product_details.price),
                cart_id = cart_id,
                product_id = product_id,
                added_by = added_by_user,
                quantity = req.data['quantity']
            )
            data_to_set.save()


        all_products = CartProducts.objects.filter(added_by=user_data['_id'])
        total = 0
        if all_products:
            for item in all_products:
                total = total + item.price

        UserCart.objects.filter(added_by=user_data['_id']).update(total=total)


    return Response("Product added successfully.")



class AddOrder(APIView):
    def post(self, request):
        pass


class CartListView(APIView):
    # parser_classes = [FormParser]

    # @swagger_auto_schema(
    #         operation_id='Get cart Products list',
    #         operation_description='Get products of cart. ',
    #         manual_parameters=products_list_user_manual_parameters + header_parameters,
    #         responses=products_list_user_responses
    # )
    def get(self, request):
        print("7777777777", request.user)
        cart_data = UserCart.objects.filter(added_by=request.user,status=1)
        # queryset = Products.objects.all()

        # if request.GET.get('search'):
        #     queryset = products.filter(name__icontains = request.GET.get('search'))
        
        # serializer = ProductSerializer(queryset, many=True)
    
        return Response('data')

