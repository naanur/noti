from dotenv import load_dotenv
import os
from noti.celery import app as celery_app
from .models import MailSend, Client, Message
import pytz
import datetime
import requests
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

load_dotenv()
EXTERNAL_API_URL = os.getenv('EXTERNAL_API_URL')
TOKEN_API = os.getenv('TOKEN_API')


@celery_app.task(bind=True, retry_backoff=True)
def send_message(self, data, client_id, mail_send_id, url=EXTERNAL_API_URL, token=TOKEN_API):
    mail_send = MailSend.objects.get(pk=mail_send_id)
    client = Client.objects.get(pk=client_id)
    timezone = pytz.timezone(client.timezone)
    now = datetime.datetime.now(timezone)

    if mail_send.pub_start <= now.time() <= mail_send.pub_end:
        header = {
            'Authorization': f'Token {token}',
            'Content-Type': 'application/json'}
        try:
            requests.post(url=url + str(data['id']), headers=header, json=data)
        except requests.exceptions.RequestException as exc:
            logger.error(f"Message if: {data['id']} is error")
            raise self.retry(exc=exc)
        else:
            logger.info(f"Message id: {data['id']}, Sending status: 'Sent'")
            Message.objects.filter(pk=data['id']).update(status='Sent')
    else:
        time = 24 - (int(now.time().strftime('%H:%M:%S')[:2]) -
                     int(mail_send.pub_start.strftime('%H:%M:%S')[:2]))
        time = 60 * 60 * time
        logger.info(f"Message id: {data['id']}, "
                    f"The current time is not suitable,"
                    f"Will retry after {time} seconds")
        return self.retry(countdown=time)
