import bcrypt
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from PIL import Image
from io import BytesIO
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


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
    


# def create_thumbnail(user_profile_image):
#         try:
#             file_content = user_profile_image.read()
#             user_profile_image_thumbnail = Image.open(user_profile_image)

#             width, height = user_profile_image_thumbnail.size
#             user_profile_image_thumbnail = user_profile_image_thumbnail.resize((width, height))    #PIL.Image.ANTIALIAS)
#             thumbnail_path = os.path.join(
#                 'images/thumbnails',
#                 f"{os.path.splitext(os.path.basename(user_profile_image.name))[0]}_thumbnail.jpg"
#             )

#             user_profile_image_thumbnail.save(thumbnail_path, format='JPEG')
#             return user_profile_image_thumbnail
#         except Exception as e:
#               print(e)


def create_thumbnail(user_profile_image):
        user_profile_image_thumbnail = Image.open(BytesIO(user_profile_image.read()))

        width, height = user_profile_image_thumbnail.size
        thumbnail_size = (width, height)

        thumbnail = user_profile_image_thumbnail.copy()
        thumbnail.thumbnail(thumbnail_size)

        thumbnail_io = BytesIO()
        thumbnail.save(thumbnail_io, format='JPEG')
    
        result_image = user_profile_image.name

        filename = os.path.basename(user_profile_image.name)
    
        filename, ext = os.path.splitext(filename)
        thumbnail_path = f"images/thumbnails/{filename}_thumbnail.jpg"
        
        user_profile_image_thumbnail1 = ContentFile(thumbnail_io.getvalue())
        user_profile_image_thumbnail1.name = thumbnail_path
        user_profile_image_thumbnail1.seek(0)

        with default_storage.open(thumbnail_path, 'wb') as destination:
            destination.write(user_profile_image_thumbnail1.read())
        # user_profile_image_thumbnail1.save(thumbnail_path, user_profile_image_thumbnail1) #ContentFile(thumbnail_io.getvalue())

        thumbnail_io.close()
        return True


def generateThumbnails():

    img = Image.open("images/can.png")
    SIZE = (75, 75)
  
    img.thumbnail(SIZE)
  
    img.save('can_thumb.png')
