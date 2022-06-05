from django.core.mail import send_mail


users_mail = 'ivan.stereotekk@gmail.com'

def send(users_mail):
    send_mail(
        'Developers happiness!',
        'You will get a much serotonin when you will see this letter.',
        'capitan.django@mail.ru',
        [users_mail],
        fail_silently=False,
    )
    return 'Sent letter successfully!'