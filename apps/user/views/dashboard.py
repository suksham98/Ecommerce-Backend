from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from django.db.models import Q
from ..models.user import CustomUser
from ...custom_admin.models.categories import Categories
from ...custom_admin.models.products import Products
from ..models.user_cart import UserCart
from ..models.cart_products import CartProducts
from ..serializer import UserSerializer, CommonSerializer, CategorySerializer
from utils.common_functions import auth
from django.shortcuts import get_object_or_404
from rest_framework import status



class CategoriesView(APIView):
    
    def get(self, request):
        categories = Categories.objects.filter(status=1)

        if request.GET.get('search'):
            search = request.GET.get('search')

            categories = categories.filter(
            Q(name__icontains = search) |
            Q(_id__icontains = search)
            )
        
        data = {'categories': [], 'products': []}
        search = request.GET.get('search')

        for category in categories:
            products = Products.objects.filter(category_id=category._id)
            product_serializer = CommonSerializer(products, many=True)
            
            data['categories'].append(CategorySerializer(category).data)
            data['products'].extend(product_serializer.data)

        return Response(data)

    


class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.filter(status=1)
        queryset = Products.objects.all()

        if request.GET.get('search'):
            queryset = products.filter(name__icontains = request.GET.get('search'))
        
        serializer = CommonSerializer(queryset, many=True)
    
        return Response(serializer.data)




class HomeView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        algorithm_used = 'HS256'
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
        except jwt.ExpiredSignatureError as e:
            raise AuthenticationFailed('Unauthenticated!') from e

        user = CustomUser.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    


class AddEditCartView(APIView):
    def post(self, request):
        user_info = auth(request)

        # Convert user ID to CustomUser instance
        user_instance = get_object_or_404(CustomUser, _id=user_info['id'])

        if cart_data := UserCart.objects.filter(added_by=user_instance).first():
            extra_vals = {'cart_id': cart_data['_id']}

        else:
            # return Response({"message": "Cart already exists"}, status=status.HTTP_200_OK)

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
    product_in_cart = CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['id']).first()

    if product_details:
        if product_in_cart:
            if req.data['quantity']==0:
                CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['id']).delete()
            elif req.data['quantity']:
                data_to_update = {}
                data_to_update.quantity = req.data['quantity']
                data_to_update.price = req.data['quantity'] * int(product_details['price'])
                CartProducts.objects.filter(product_id=req.data['product_id'], added_by=user_data['id']).update(data_to_update)

        else:
            added_by_user =  get_object_or_404(CustomUser, _id=user_data['id'])
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


        all_products = CartProducts.objects.filter(added_by=user_data['id'])
        total = 0
        if all_products:
            for item in all_products:
                total = total + item.price

        UserCart.objects.filter(added_by=user_data['id']).update(total=total)


    return Response("Product added successfully.")



class AddOrder(APIView):
    def post(self, request):
        pass
