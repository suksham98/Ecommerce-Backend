from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse, JsonResponse
# from django.http import JsonResponse
import jwt, datetime
from apps.user.models.user import CustomUser
from apps.user.serializer import CommonUserSerializer


# class AuthMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.specific_paths = ['/user/user_products/', '/user/categories/', '/user/add_edit_cart/', '/user/home/']

#     def __call__(self, request):
        
#         if request.path in self.specific_paths:
#             try:
                
#                 token = request.headers.get('Authorization')

#                 if not token:
#                     raise AuthenticationFailed('Unauthenticated!')

#                 # token = token.split(' ')[1]
#                 algorithm_used = 'HS256'

#                 payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
                
#                 request.user = payload
#                 user_data = CustomUser.objects.filter(_id=payload['id']).first()
#                 user_serializer = CommonUserSerializer(user_data)
#                 print("444444444444444444555555555555", user_serializer.data)
#                 if user_serializer.data['_id']:
#                     response = self.get_response(request)
#                     print("rrrrrrrrrrrrresponse", response)
                
#                     return response

#             except jwt.ExpiredSignatureError as e:
#                 raise AuthenticationFailed('Token has expired!') from e
#             except jwt.InvalidTokenError as e:
#                 raise AuthenticationFailed('Invalid token!') from e
#         response = self.get_response(request)

#         print("1111111111111",response)
#         return response



class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.specific_paths = ['/user/categories/', '/user/home/'] #'/user/user_products/', '/user/add_edit_cart/',

    def __call__(self, request):
        
        if request.path in self.specific_paths:
            try:
                token = request.headers.get('Authorization')
                if not token:
                    return JsonResponse({'error': 'Unauthenticated!'}, status=401)

                # if not token:
                #     raise AuthenticationFailed('Unauthenticated!')

                algorithm_used = 'HS256'

                payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
                
                # request.user = payload
                user_data = CustomUser.objects.filter(_id=payload.get('id')).first()
                # print("88888", user_data)

                if user_data:
                    user_serializer = CommonUserSerializer(user_data)
                    request.user = user_serializer.data
                    # print(user_serializer.data)
                    
                    if '_id' in user_serializer.data:
                        response = self.get_response(request)
                        # print("333333333333333333333", payload, request.user)
                        return response
                    else:
                        raise AuthenticationFailed('User data is incomplete!')
                else:
                    raise AuthenticationFailed('User not found!')

            except jwt.ExpiredSignatureError as e:
                raise JsonResponse({'error': 'Token has expired!'}, status=402)
            except jwt.InvalidTokenError as e:
                raise AuthenticationFailed('Invalid token!') from e

        response = self.get_response(request)
        return response
