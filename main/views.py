from django.shortcuts import render

from .models import MailSend, Client, Message
from django.contrib.auth.models import User
from .serializers import MailSendSerializer, ClientSerializer, MessageSerializer, UserSerializer

from rest_framework import viewsets, permissions


# viewset for User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# viewset for MailSend model
class MailSendViewSet(viewsets.ModelViewSet):
    queryset = MailSend.objects.all()
    serializer_class = MailSendSerializer
    permission_classes = [permissions.IsAuthenticated]


# viewset for Client model
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]


# viewset for Message model
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]