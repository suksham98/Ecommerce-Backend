import bcrypt
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from PIL import Image
from io import BytesIO
import os
from django.http import HttpResponse, JsonResponse
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message
from apps.user.models.user import CustomUser



def hash_password(password): 
    byte = password.encode('utf-8')
    salt = bcrypt.gensalt() 

    return bcrypt.hashpw(byte, salt)
  


def check_password(password, userPassword):

    byte = password.encode('utf-8') 

    salt = bcrypt.gensalt() 

    hashed = bcrypt.hashpw(byte, salt)  
    userBytes = userPassword.encode('utf-8') 
    # print(bcrypt.checkpw(userBytes, hashed))
    return bcrypt.checkpw(userBytes, hashed)


from functools import wraps
from rest_framework.response import Response
from rest_framework import status


# def auth(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         # Check if the object passed as request is a valid HttpRequest
#         if not hasattr(request, 'headers') or not callable(getattr(request, 'headers', None)):
#             return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

#         token = request.headers.get('Authorization')
#         if not token:
#             return Response({'error': 'Missing Authorization header'}, status=status.HTTP_401_UNAUTHORIZED)

#         try:
#             response = view_func(request, *args, **kwargs)
#         except Exception as e:
#             return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         return response

#     return _wrapped_view



# def auth(request):
#     token = request.headers.get('Authorization')

#     algorithm_used = 'HS256'

#     if not token:
#             raise AuthenticationFailed('Unauthenticated!')

#     try:
#         # decoded_token = jwt.decode(token, verify=False)
#         decoded_token = jwt.decode(token, 'secret', algorithms=[algorithm_used])

#         return decoded_token
    
#     except jwt.ExpiredSignatureError as e:
#             raise JsonResponse({'error': 'Token has expired!'}, status=402)
#     except Exception as e:
#          print(e)
#          raise JsonResponse({"error": "Some error occurred"})



def auth(request):
        from apps.user.serializer import CommonUserSerializer
        try:
                token = request.headers.get('Authorization')
            
                if not token:
                    raise AuthenticationFailed('Unauthenticated!')

                algorithm_used = 'HS256'

                payload = jwt.decode(token, 'secret', algorithms=[algorithm_used])
                
                user_data = CustomUser.objects.filter(_id=payload.get('id')).first()

                if user_data:
                    user_serializer = CommonUserSerializer(user_data)
                    request.user = user_serializer.data
                    # print(user_serializer.data)
                    
                    if '_id' in user_serializer.data:
                        response = request
                        # print("333333333333333333333", payload)
                        return response
                    else:
                        raise AuthenticationFailed('User data is incomplete!')
                else:
                    raise AuthenticationFailed('User not found!')

        except jwt.ExpiredSignatureError as e:
                return HttpResponse({'error': 'Token has expired!'})
        except jwt.InvalidTokenError as e:
                return HttpResponse({'error': 'Invalid Token!'})

        # response = self.get_response(request)
        # return response



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
