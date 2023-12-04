from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ..serializer import UserSerializer, CommonSerializer, CommonUserSerializer
from rest_framework.response import Response
from utils.common_functions import hash_password
from ..models import CustomUser
from ...custom_admin.admin_models.categories import Categories
from ...custom_admin.admin_models.products import Products

from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime



@api_view(['POST'])
def signup(request):
    print("Template directories:", settings.TEMPLATES[0]['DIRS'])
    print(request.data)
    return render(request, 'apps/user/signup.html')


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = hash_password(request.data['password'])
        serializer.password = password 
        serializer.save()

        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()
        print(user)
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Email or password is incorrect!')

        payload = {
            "id": str(user._id),
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.timezone.utc),
        }
        profile_image_url = None
        if user.user_profile_image:
            profile_image_url = request.build_absolute_uri(user.user_profile_image.url)

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        user_data = {
            '_id':user._id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'phone_number':user.phone_number,
            'user_profile_image':profile_image_url,
        }
        
        
        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'token': token,
            'user' : user_data
        }
        return response



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

        user = CustomUser.objects.filter(_id=payload['_id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)
    


class ProductsView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        algorithm_used = 'HS256'
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
        except jwt.ExpiredSignatureError as e:
            raise AuthenticationFailed('Unauthenticated!') from e

        # categories = Categories.objects.filter(status=1)
        # serializer = CommonSerializer(categories, many=True)
        products = Products.objects.filter(status=1)
        serializer = CommonSerializer(products, many=True)
        # data = {
        #     'Categories' : serializer.data,
        #     'Products' : serializer1.data
        # }
        # print(serializer.data['category_id'])
        return Response(serializer.data)
    



class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'successfully logged out'
        }
        return response