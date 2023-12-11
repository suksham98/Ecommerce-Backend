from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from fcm_django.models import FCMDevice
from django.http import JsonResponse
from utils.common_functions import send_push_notification
   


@api_view(['GET'])
def send_notification_view(request):

    device_token = 'eEX1IDr0SKCGhaFn30ljf8:APA91bH3S7isbJiWjXbABilATM3DYqnotfipeHCAksBhIZhzvXnFFB13tsq54WJICrSVgcBF1BrJVC2DCoM9b_ThVUBexG-BimblJXcNmJq-SFdyP6LNDfMg1MUYfNaB4lOdHAuOleq3'

    notification_data = {'title': 'New Message', 'body': 'You have a new message!'}

    send_push_notification(device_token, notification_data)

    return JsonResponse({'message': 'Notification sent successfully!'})



class RegisterDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # device_token1 = request.data['device_token']
        device_token = 'eEX1IDr0SKCGhaFn30ljf8:APA91bH3S7isbJiWjXbABilATM3DYqnotfipeHCAksBhIZhzvXnFFB13tsq54WJICrSVgcBF1BrJVC2DCoM9b_ThVUBexG-BimblJXcNmJq-SFdyP6LNDfMg1MUYfNaB4lOdHAuOleq3'

        FCMDevice.objects.create(registration_id=device_token)
        return JsonResponse({'status': 'Device registered successfully!'})