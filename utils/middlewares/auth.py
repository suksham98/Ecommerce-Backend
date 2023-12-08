from rest_framework.exceptions import AuthenticationFailed
from django.http import HttpResponse
import jwt, datetime


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.specific_paths = ['/user/user_products/', '/user/categories/', '/user/add_edit_cart/', '/user/home/']

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.path in self.specific_paths:
            
              token = request.COOKIES.get('jwt')
              token1 = request.headers['jwt']
              algorithm_used = 'HS256'

              if not token1:
                 raise AuthenticationFailed('Unauthenticated!')

              try:
                payload = jwt.decode(token1, 'secret', algorithms=[algorithm_used])
                response.payload = payload
    
              except jwt.ExpiredSignatureError as e:
                 print(e)
                 raise AuthenticationFailed('Unauthenticated!') from e
            


        return response