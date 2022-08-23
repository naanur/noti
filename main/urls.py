from django.urls import path, include, re_path
from rest_framework import routers, permissions


from .views import *


app_name = 'main'
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'mailsends', MailSendViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'messages', MessageViewSet)


urlpatterns = [

    path('', include(router.urls)),

]