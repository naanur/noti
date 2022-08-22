from django.contrib import admin

# Register your models here.
from .models import MailSend, Client, Message

admin.site.register(MailSend)
admin.site.register(Client)
admin.site.register(Message)