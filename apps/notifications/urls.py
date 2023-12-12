from django.urls import include, path
from django.views.generic import TemplateView
from .views import DeviceDetailView, send_notifications, send_notification, send_notification_view, register_device, RegisterDeviceView

urlpatterns = [
    path("firebase-messaging-sw.js",
        TemplateView.as_view(
            template_name="firebase-messaging-sw.js",
            content_type="application/javascript",
        ),
        name="firebase-messaging-sw.js"
    ),
    path("device_details/", DeviceDetailView.as_view),
    path("notify/", send_notifications),
    path("send_notification/", send_notification_view),
    path("register_device/", RegisterDeviceView.as_view())

]