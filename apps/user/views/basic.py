from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from ..serializer import UserSerializer, CommonSerializer, CommonUserSerializer
from rest_framework.response import Response
from utils.common_functions import hash_password, create_thumbnail
from ..models.user import CustomUser
from ...custom_admin.models.categories import Categories
from ...custom_admin.models.products import Products
from services.user_services.swagger import *

from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser, FileUploadParser
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework import status
from django.http import HttpResponse


#Class to handle registration view for users
class RegisterView(APIView):
    # parser_classes = [MultiPartParser, FormParser, JSONParser, FileUploadParser]
    parser_classes = [MultiPartParser, FormParser]

    @swagger_auto_schema(
            operation_id='Register a new user',
            operation_description='Registering new user by providing various information. ',
            manual_parameters=register_user_manual_parameters,
            responses=register_user_responses
        )
    def post(self, request, *args, **kwargs):
       
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = hash_password(request.data['password'])
 
        serializer.password = password
        serializer.save()
        
        return Response(serializer.data)


#Class to handle User Login 
class LoginView(APIView):
    parser_classes = [FormParser]

    @swagger_auto_schema(
            operation_id='User Login',
            operation_description='Login User with email and password. ',
            manual_parameters=login_user_manual_parameters,
            responses=login_user_responses
        )
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()
        
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

        profile_image_thumbnail_url = None
        if user.user_profile_image:
            profile_image_thumbnail_url = request.build_absolute_uri(user.user_profile_image_thumbnail.url)


        token = jwt.encode(payload, 'secret', algorithm='HS256')
        user_data = {
            '_id':user._id,
            'first_name':user.first_name,
            'last_name':user.last_name,
            'email':user.email,
            'phone_number':user.phone_number,
            'user_profile_image':profile_image_url,
            'user_profile_image_thumbnail':profile_image_thumbnail_url
        }
        
        
        response = Response()

        # response.set_cookie(key='Authorization', value=token, httponly=True)
        response['Authorization'] =  token
        response.data = {
            'token': token,
            'user' : user_data
        }
        return response
   

#Class to handle User Logout
class LogoutView(APIView):

    @swagger_auto_schema(
            operation_id='User Logout',
            operation_description='User Logout. ',
            manual_parameters=logout_user_manual_parameters,
            responses=logout_user_responses
    )
    def post(self, request):
        print(request.COOKIES.get('Authorization'))

        response = Response()
        response.delete_cookie('Authorization')
        response.data = {
            'message': 'successfully logged out'
        }
        return response
