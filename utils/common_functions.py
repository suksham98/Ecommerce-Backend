import bcrypt
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime


def hash_password(password): 
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt() 

    return bcrypt.hashpw(byte, salt)
  


def check_password(password, userPassword):

    byte = password.encode('utf-8') 

    salt = bcrypt.gensalt() 

    hashed = bcrypt.hashpw(byte, salt)  
    userBytes = userPassword.encode('utf-8') 
    print(bcrypt.checkpw(userBytes, hashed))
    return bcrypt.checkpw(userBytes, hashed)


def auth(request):
    token = request.COOKIES.get('jwt')
    algorithm_used = 'HS256'

    if not token:
            raise AuthenticationFailed('Unauthenticated!')

    try:
        return jwt.decode(token, 'secret', algorithms=[algorithm_used])
    
    except jwt.ExpiredSignatureError as e:
            raise AuthenticationFailed('Unauthenticated!') from e