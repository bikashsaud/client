from django.db import models
from django.db.models.signals import post_save, pre_save
from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
# Create your models here.

# from django.utils.text import slugify  
class Client(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    client_email = models.EmailField()

    def __str__(self):
        return self.client_name

def save_client(sender, instance, **kwargs):
    to_email = instance.client_email
    subject = 'Your Message is Received !!!'
    from_email = settings.EMAIL_HOST_USER
    print(instance.client_email, '     post_save mail send')
    body = f'Dear sir, \n Your Profile created with this mail. \n CEO...'
    send_mail(subject, body, from_email, [to_email], fail_silently=True)

post_save.connect(save_client, sender=Client)


