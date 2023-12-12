import bcrypt
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from PIL import Image
from io import BytesIO
import os
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message


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
    token = request.COOKIES.get('Authorization')
    algorithm_used = 'HS256'

    if not token:
            raise AuthenticationFailed('Unauthenticated!')

    try:
        raw_token = token.replace("Bearer ", "")
        print(raw_token)
        decoded_token = jwt.decode(raw_token, verify=False)
        return jwt.decode(decoded_token, 'secret', algorithms=[algorithm_used])
    
    except jwt.ExpiredSignatureError as e:
            raise AuthenticationFailed('Unauthenticated!') from e
    

def create_thumbnail(user_profile_image):
        user_profile_image_thumbnail = Image.open(BytesIO(user_profile_image.read()))

        width, height = user_profile_image_thumbnail.size
        thumbnail_size = (width, height)

        thumbnail = user_profile_image_thumbnail.copy()
        thumbnail.thumbnail(thumbnail_size)

        thumbnail_io = BytesIO()
        thumbnail.save(thumbnail_io, format='JPEG')

        filename = os.path.basename(user_profile_image.name)
    
        filename, ext = os.path.splitext(filename)
        thumbnail_path = f"images/thumbnails/{filename}_thumbnail.jpg"
        
        user_profile_image_thumbnail1 = ContentFile(thumbnail_io.getvalue())
        user_profile_image_thumbnail1.name = thumbnail_path
        user_profile_image_thumbnail1.seek(0)

        with default_storage.open(thumbnail_path, 'wb') as destination:
            destination.write(user_profile_image_thumbnail1.read())

        thumbnail_io.close()
        return True

# This static function was just for testing purposes
def generateThumbnails():

    img = Image.open("images/can.png")
    SIZE = (75, 75)
  
    img.thumbnail(SIZE)
  
    img.save('can_thumbnail.png')



def send_push_notification(device_token, message_data):
    """
    Send a push notification to a device.
    :param device_token: The device token to send the notification to.
    :param message_data: The data to include in the notification.
    """
    try:
        device = FCMDevice.objects.get(registration_id=device_token)

        message = Message(data=message_data)

        msg = device.send_message(message)
        print(msg)
        print(f"Notification sent successfully to {device_token}")
    except FCMDevice.DoesNotExist:
        print(f"Device with token {device_token} not found.")
    except Exception as e:
        print(f"Error sending notification: {str(e)}")
