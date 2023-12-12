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
            
              # token1 = request.COOKIES.get('Authorization')
              token = request.headers['Authorization']

              if not token or not token.startswith('Bearer '):
                  raise AuthenticationFailed('Unauthenticated!')

              token2 = token.split(' ')[1]

              algorithm_used = 'HS256'

              try:
                print(token2)
                payload = jwt.decode(token2, 'secret', algorithms=[algorithm_used])
                print(payload)
                import datetime

                exp_timestamp = payload['exp']
                iat_timestamp = payload['iat']

               # Convert Unix timestamps to datetime objects
                exp_datetime = datetime.datetime.utcfromtimestamp(exp_timestamp)
                iat_datetime = datetime.datetime.utcfromtimestamp(iat_timestamp)

                exp_local = exp_datetime.replace(tzinfo=datetime.timezone.utc).astimezone()
                iat_local = iat_datetime.replace(tzinfo=datetime.timezone.utc).astimezone()

               # Print the local time
                print(f'exp (local time): {exp_local}')
                print(f'iat (local time): {iat_local}')

                response.payload = payload
    
              except jwt.ExpiredSignatureError as e:
                 print(e)














                 
                 raise AuthenticationFailed('Token has expired!') from e
            

        return response
