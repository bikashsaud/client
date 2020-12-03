from client_app.models import Client
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from django_seed import Seed
seeder = Seed.seeder()
class Command(BaseCommand):
    help = 'create 10 clients'


    def handle(self, *args, **kwargs):
        Client.objects.all().delete()
        total_client = 10
        for i in range(total_client):
            Client.objects.create(client_name=get_random_string(), client_email=seeder.faker.email())
        
