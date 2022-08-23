from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import MailSend, Client, Message
from django.contrib.auth.models import User
from .serializers import MailSendSerializer, ClientSerializer, MessageSerializer, UserSerializer

from rest_framework import viewsets, permissions


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


# viewset for MailSend model
class MailSendViewSet(viewsets.ModelViewSet):
    queryset = MailSend.objects.all()
    serializer_class = MailSendSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'])
    def info(self, request, pk=None):
        """
        Summary data for a specific mailsend list
        """
        queryset_mailsend = MailSend.objects.all()
        get_object_or_404(queryset_mailsend, pk=pk)
        queryset = Message.objects.filter(mail_send=pk).all()
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def fullinfo(self, request):
        total_count = MailSend.objects.count()
        mailsend = MailSend.objects.values('id')
        content = {'Total number of mailsend': total_count,
                   'The number of messages sent': ''}
        result = {}

        for row in mailsend:
            res = {'Total messages': 0, 'Sent': 0, 'No sent': 0}
            message = Message.objects.filter(mail_send=row['id']).all()
            group_sent = message.filter(status='Sent').count()
            group_no_sent = message.filter(status='Not send').count()
            res['Total messages'] = len(message)
            res['Sent'] = group_sent
            res['No sent'] = group_no_sent
            result[row['id']] = res

        content['The number of messages sent'] = result
        return Response(content)


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


def index(request):
    return render(request, 'index.html')
