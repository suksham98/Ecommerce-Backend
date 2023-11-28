from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .serializer import UserSerializer
from rest_framework.response import Response
from utils.common_functions import hash_password, check_password
from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
@api_view(['POST'])
def signup(request):
    print("Template directories:", settings.TEMPLATES[0]['DIRS'])
    print(request.data)
    return render(request, 'apps/user/signup.html')



# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']
#         user = User.objects.get(email=email, password=password)
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['name'] = "%s %s" % (
#                     user.first_name, user.last_name)
#                 user_details['token'] = token
#                 user_logged_in.send(sender=user.__class__,
#                                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)
#             except Exception as e:
#                 raise e
#         else:
#             res = {
#                 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
#             return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = {'error': 'please provide a email and a password'}
#         return Response(res)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        password = hash_password(request.data['password'])
        serializer.password = password 
        serializer.save()

        return Response(serializer.data)

# @api_view(['POST'])
# def register(request):
#     print(request)
#     return Response(request.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Email or password is incorrect!')

        payload = {
            "id": user.id,
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now(datetime.timezone.utc),
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        # response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'token': token
        }
        return response
        
        # return Response({
        #     "message":"success"
        # })
        