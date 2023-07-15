from django.core.mail import send_mail
from root.settings import EMAIL_HOST_USER


def send_email(email,message):

    send_mail(
        subject= "hello",
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=["shohsanam.obidova27@gmail.com"],
        fail_silently=False,

    )
