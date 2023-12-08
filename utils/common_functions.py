import bcrypt
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from PIL import Image
from io import BytesIO
import os


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
    


def create_thumbnail(user_profile_image):
        try:
            file_content = user_profile_image.read()
            user_profile_image_thumbnail = Image.open(user_profile_image)

            width, height = user_profile_image_thumbnail.size
            user_profile_image_thumbnail = user_profile_image_thumbnail.resize((width, height))    #PIL.Image.ANTIALIAS)
            thumbnail_path = os.path.join(
                'images/thumbnails',
                f"{os.path.splitext(os.path.basename(user_profile_image.name))[0]}_thumbnail.jpg"
            )

            user_profile_image_thumbnail.save(thumbnail_path, format='JPEG')
            return user_profile_image_thumbnail
        except Exception as e:
              print(e)



def generateThumbnails():

    img = Image.open("images/can.png")
    SIZE = (75, 75)
  
    img.thumbnail(SIZE)
  
    img.save('can_thumb.png')
