"""
Author:
ivan Goncharov
ivan.stereotekk@gmail.com
telegram: @EwanPotterman
"""

from django.core.mail import send_mail


mail_to = 'ivan.stereotekk@gmail.com'
text = None
subject =None
sender = 'capitan.django@mail.ru'

def send(subject,text,sender,mail_to):
    send_mail(
        subject,
        text,
        sender,
        [mail_to],
        fail_silently=False,
    )
    return 'Sent letter successfully!'