from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import MailSend, Client, Message


# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="main:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MailSendSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="main:mailsend-detail")

    class Meta:
        model = MailSend
        fields = ['url', 'id', 'text', 'pub_start', 'pub_end']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
