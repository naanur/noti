from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import MailSend, Client, Message


# Serializers define the API representation.

class UserSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="main:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MailSendSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="main:mailsend-detail")

    class Meta:
        model = MailSend
        fields = ['id', 'pub_start', 'pub_end', 'text', 'mobile_code', 'client_tag']


class ClientSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="main:client-detail")

    class Meta:
        model = Client
        fields = ['id', 'phone', 'mobile_code', 'tag']


class MessageSerializer(serializers.ModelSerializer):
    # url = serializers.HyperlinkedIdentityField(view_name="main:message-detail")

    class Meta:
        model = Message
        fields = ['id', 'pub_date', 'client', 'mail_send', 'url', 'status']
