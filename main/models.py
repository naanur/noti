from django.db import models
from django.core.validators import RegexValidator
import pytz


class MailSend(models.Model):
    """
    Сущность "рассылка" имеет атрибуты:
    -уникальный id рассылки
    -дата и время запуска рассылки
    -текст сообщения для доставки клиенту
    -фильтр свойств клиентов, на которых должна быть произведена рассылка (код мобильного оператора, тег)
    -дата и время окончания рассылки. никакие сообщения клиентам после этого времени доставляться не должны
    """
    pub_start = models.DateTimeField()
    pub_end = models.DateTimeField()
    text = models.TextField(max_length=512)
    mobile_code = models.CharField(max_length=3)
    client_tag = models.CharField(max_length=100)

    def __str__(self):
        return f"#{self.id} MailSend от {self.pub_start} до {self.pub_end}"


class Client(models.Model):
    """
    Сущность "клиент" имеет атрибуты:
    -уникальный id клиента
    -номер телефона клиента в формате 7XXXXXXXXXX(X - цифра от 0 до 9)
    -код мобильного оператора
    -тег(произвольная метка)
    -часовой пояс
    """
    phone_validator = RegexValidator(regex=r'^\d{10}$', message="Phone must be in format: '7XXXXXXXXXX'.")

    phone = models.CharField(max_length=11, unique=True, validators=[phone_validator])
    mobile_code = models.CharField(max_length=3, editable=False)
    tag = models.CharField(max_length=100)

    TIMEZONE_CHOICES = zip(pytz.all_timezones, pytz.all_timezones)
    timezone = models.CharField(max_length=255, default='UTC', blank=True, choices=TIMEZONE_CHOICES)

    def __str__(self):
        return f"#{self.id} Client {self.mobile_code} {self.phone}"

    def save(self, *args, **kwargs):
        self.mobile_code = self.phone[:3]
        super(Client, self).save(*args, **kwargs)


class Message(models.Model):
    """
    Сущность "сообщение" имеет атрибуты:
    -уникальный id сообщения
    -дата и время отправки сообщения
    -статус отправки
    -id клиента, которому отправлено сообщение
    -id рассылки, которая отправила сообщение
    """

    pub_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mail_send = models.ForeignKey(MailSend, on_delete=models.CASCADE)


    SEND_STATUS_CHOICES = [
        ('S', 'Sent'),
        ('F', 'Failed'),
        ('D', 'Delivered'),
        ('U', 'Undelivered'),
        ('N', 'Not sent'),
    ]

    status = models.CharField(max_length=10, default='N', choices=SEND_STATUS_CHOICES)

    def __str__(self):
        return f"#{self.id} Message from MailSend{self.mail_send} to {self.client}"
