from django.urls import include, path
from django.views.generic import TemplateView
from .views import send_notification_view, RegisterDeviceView

urlpatterns = [
    path("send_notification/", send_notification_view),
    path("register_device/", RegisterDeviceView.as_view())

]