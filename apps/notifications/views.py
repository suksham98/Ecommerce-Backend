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


class DeviceDetailView(APIView):
    def post(self, request, *args, **kwargs):
        device_type = request.data['device_type']
        user = self.request.user
        device_id = request.data['device_id']
        registration_id = request.data['registration_id']
    #     gcm_device = FCMDevice.objects.get_or_create(
    #         device_id=device_id,
    #         registration_id=registration_id,
    #         user=user,
    #         cloud_message_type="FCM"
    # )
        

@api_view(['GET'])
def send_notifications(request):
    devices = FCMDevice.objects.filter(active=True)
    # gcm_devices = GCMDevice.objects.filter(active=True) # Or whatever filter you want
    devices.send_message(
        "This is a demo notification for testing",
        title="Notification"
    )

# topic = "A topic"
# topic_name = 'New Products'
# # FCMDevice.objects.handle_subscription(True, topic)
# FCMDevice.send_topic_message(Message(data={"data":"hello world"}), topic_name)
# FCMDevice.objects.send_message(Message(data=dict()))
# # Note: You can also combine the data and notification kwarg
# FCMDevice.objects.send_message(
#     Message(notification=Notification(title="title", body="body", image="image_url"))
# )
# device = FCMDevice.objects.first()
# device.send_message(Message("hello"))


# You can still use .filter() or any methods that return QuerySet (from the chain)
# device = FCMDevice.objects.all().first()
# send_message parameters include: message, dry_run, app
# device.send_message(Message(data={...}))

def send_notification(self):
    # devices = CustomFCMDevice.objects.all()
    print("send_notifications")
    FCMDevice.send_topic_message(Message(data={"a":"b"}), "topic")
    print(FCMDevice)
    return HttpResponse("success")



@api_view(['GET'])
def send_notification_view(request):
    # devices = FCMDevice.objects.filter(active=True)
    # devices.send_message(
    #     "This is a demo notification for testing",
    #     title="Notification"
    # )
    
    device_token = 'eEX1IDr0SKCGhaFn30ljf8:APA91bH3S7isbJiWjXbABilATM3DYqnotfipeHCAksBhIZhzvXnFFB13tsq54WJICrSVgcBF1BrJVC2DCoM9b_ThVUBexG-BimblJXcNmJq-SFdyP6LNDfMg1MUYfNaB4lOdHAuOleq3'
    # 'cpI0E8v-hkxolipfq2E1JB:APA91bEH49Hy5mkwpEPtBOcQ9AB8ed7DU2DHWAaWRt_SATogrrfppYSzG6WPURloMpTUM8UOafbxc-ULjAte2iAB2ckFQkRpLdaPd9ZfiSZYeGMOSqH3J1nn5YSMwZQ4TrQuQmsskhsy'

    notification_data = {'title': 'New Message', 'body': 'You have a new message!'}

    send_push_notification(device_token, notification_data)

    return JsonResponse({'message': 'Notification sent successfully!'})



@api_view(['GET'])
def register_device(request):
    device_token = 'cpI0E8v-hkxolipfq2E1JB:APA91bEH49Hy5mkwpEPtBOcQ9AB8ed7DU2DHWAaWRt_SATogrrfppYSzG6WPURloMpTUM8UOafbxc-ULjAte2iAB2ckFQkRpLdaPd9ZfiSZYeGMOSqH3J1nn5YSMwZQ4TrQuQmsskhsy'

    FCMDevice.objects.create(registration_id=device_token)
    return JsonResponse({'status': 'Device registered successfully!'})


class RegisterDeviceView(APIView):
    def get(self, request, *args, **kwargs):
        # device_token1 = request.data['device_token']
        device_token = 'eEX1IDr0SKCGhaFn30ljf8:APA91bH3S7isbJiWjXbABilATM3DYqnotfipeHCAksBhIZhzvXnFFB13tsq54WJICrSVgcBF1BrJVC2DCoM9b_ThVUBexG-BimblJXcNmJq-SFdyP6LNDfMg1MUYfNaB4lOdHAuOleq3'
        # 'cpI0E8v-hkxolipfq2E1JB:APA91bEH49Hy5mkwpEPtBOcQ9AB8ed7DU2DHWAaWRt_SATogrrfppYSzG6WPURloMpTUM8UOafbxc-ULjAte2iAB2ckFQkRpLdaPd9ZfiSZYeGMOSqH3J1nn5YSMwZQ4TrQuQmsskhsy'

        FCMDevice.objects.create(registration_id=device_token)
        return JsonResponse({'status': 'Device registered successfully!'})
