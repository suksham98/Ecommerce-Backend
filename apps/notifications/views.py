from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from .models import CustomFCMDevice
from rest_framework.response import Response
from django.http import JsonResponse
from utils.common_functions import send_push_notification


@api_view(['GET'])
def send_notification_view(request):
    # devices = FCMDevice.objects.filter(active=True)
    # devices.send_message(
    #     "This is a demo notification for testing",
    #     title="Notification"
    # )
    
    device_token = 'your_device_token_here'
    notification_data = {'title': 'New Message', 'body': 'You have a new message!'}

    send_push_notification(device_token, notification_data)

    return JsonResponse({'message': 'Notification sent successfully!'})


class RegisterDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # device_token1 = request.data['device_token']
        device_token = 'your_device_token_here'

        FCMDevice.objects.create(registration_id=device_token)
        return JsonResponse({'status': 'Device registered successfully!'})
