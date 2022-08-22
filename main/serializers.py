from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import MailSend, Client, Message


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class MailSendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailSend
        fields = ['id', 'pub_start', 'pub_end', 'text', 'mobile_code', 'client_tag']


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'phone', 'mobile_code', 'tag']


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'pub_date', 'client', 'mail_send']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
