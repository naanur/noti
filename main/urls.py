from django.urls import path, include
from rest_framework import routers
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'mailsends', MailSendViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]