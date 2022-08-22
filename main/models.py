from django.db import models


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
    phone = models.CharField(max_length=12)
    mobile_code = models.CharField(max_length=3)
    tag = models.CharField(max_length=100)
    timezone = models.CharField(max_length=100, default='Europe/Moscow', blank=True)

    def __str__(self):
        return f"#{self.id} Client {self.mobile_code} {self.phone}"


class Message(models.Model):
    """
    Сущность "сообщение" имеет атрибуты:
    -уникальный id сообщения
    -текст сообщения
    -дата и время отправки сообщения
    -клиент, которому отправлено сообщение
    """
    text = models.TextField(max_length=512)
    pub_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    mail_send = models.ForeignKey(MailSend, on_delete=models.CASCADE)

    def __str__(self):
        return f"#{self.id} Message {self.text} to {self.client}"
