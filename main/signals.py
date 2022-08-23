import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import MailSend, Client, Message
from .tasks import send_message
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@receiver(post_save, sender=MailSend, dispatch_uid="create_message")
def create_message(sender, instance, created, **kwargs):
    if created:
        mail_send = MailSend.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(Q(mobile_code=mail_send.mobile_code) |
                                        Q(tag=mail_send.client_tag)).all()

        print("clients: ", clients)
        print("mail_send: ", mail_send)

        for client in clients:
            m = Message.objects.create(
                status="N",
                client=client,
                mail_send=instance
            )
            m.save()
            instance.save()
            print(m)
            # message = Message.objects.filter(mail_send=instance.id, client=client.id).first()
            message = get_object_or_404(Message, mail_send=instance.id, client=client.id)
            data = {
                'id': message.id,
                "phone": client.phone,
                "text": mail_send.text
            }
            client_id = client.id
            mail_send_id = mail_send.id

            if instance.to_send:

                r = send_message.apply_async((data, client_id, mail_send_id),
                                             expires=mail_send.pub_end)

            else:
                r = send_message.apply_async((data, client_id, mail_send_id),
                                             eta=mail_send.pub_start, expires=mail_send.pub_end)

