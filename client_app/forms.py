from django import forms
from .models import *

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_email', ]


        