from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from .models import Client

def send_emails():
    email_list = Client.objects.values_list('client_emails', flat=True)
    set_email = set(email_list)
    list_email = list(set_email)
    print(list_email)
    subject = 'Your Message is Received !!!'
    from_email = settings.EMAIL_HOST_USER
    body = f'Dear sir, \n It is your office time. \n CEO...'
    send_mail(subject, body, from_email, [list_email], fail_silently=True)

