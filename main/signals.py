from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

from .models import MailSend, Client, Message
from .tasks import send_message


@receiver(post_save, sender=MailSend, dispatch_uid="create_message")
def create_message(sender, instance, created, **kwargs):
    if created:
        mail_send = MailSend.objects.filter(id=instance.id).first()
        clients = Client.objects.filter(Q(mobile_code=mail_send.mobile_operator_code) |
                                        Q(tag=mail_send.tag)).all()

        for client in clients:
            Message.objects.create(
                status="N",
                client=client.id,
                mail_send=instance.id
            )
            message = Message.objects.filter(mai_send=instance.id, client=client.id).first()
            data = {
                'id': message.id,
                "phone": client.phone_number,
                "text": mail_send.text
            }
            client = client.id
            mail_send = mail_send.id

            if instance.to_send:
                send_message.apply_async((data, client, mail_send),
                                         expires=mail_send.date_end)
            else:
                send_message.apply_async((data, client, mail_send),
                                         eta=mail_send.date_start, expires=mail_send.date_end)
