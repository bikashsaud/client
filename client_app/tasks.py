# Create your tasks here
#
from .email_service import send_emails

# ----------------------------
from celery.decorators import task
from celery import shared_task

@shared_task 
def send_notifiction():
    # this task run at 10am
    send_emails()