from django.test import TestCase
from .models import MailSend, Client, Message


class MailSendTest(TestCase):
    def test_mail_send_str(self):
        mail_send = MailSend.objects.create(pub_start='2022-01-01T00:00:00Z', pub_end='2020-01-01T00:00:00Z',
                                            text='test', mobile_code='7', client_tag='test')
        self.assertEqual(str(mail_send), f"#{mail_send.id} MailSend от {mail_send.pub_start} до {mail_send.pub_end}")


class ClientTest(TestCase):
    def test_client_str(self):
        client = Client.objects.create(phone='79999999999', mobile_code='7', tag='test')
        self.assertEqual(str(client), f"#{client.id} Client {client.mobile_code} {client.phone}")


class MessageTest(TestCase):
    def test_message_str(self):
        client = Client.objects.create(phone='79999999999', mobile_code='7', tag='test')
        mail_send = MailSend.objects.create(pub_start='2020-01-01T00:00:00Z', pub_end='2020-01-01T00:00:00Z',
                                            text='test', mobile_code='7', client_tag='test')
        message = Message.objects.create(text='test', pub_date='2020-01-01T00:00:00Z', client=client,
                                         mail_send=mail_send)
        self.assertEqual(str(message), f"#{message.id} Message {message.text} to {message.client}")


