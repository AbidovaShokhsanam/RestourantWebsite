from .services import send_email

from celery import shared_task



@shared_task
def send_email_customer(email, message):
    send_email(email, message)