from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
import jwt, datetime


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.specific_paths = ['/user/user_products/', '/user/categories/', '/user/add_edit_cart/', '/user/home/']

    def __call__(self, request):
        
        if request.path in self.specific_paths:
            try:
                
                token = request.headers.get('Authorization')

                if not token:
                    raise AuthenticationFailed('Unauthenticated!')

                # token = token.split(' ')[1]
                algorithm_used = 'HS256'

                payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
                
                request.user = payload

            except jwt.ExpiredSignatureError as e:
                raise AuthenticationFailed('Token has expired!') from e
            except jwt.InvalidTokenError as e:
                raise AuthenticationFailed('Invalid token!') from e

        response = self.get_response(request)

        return response
