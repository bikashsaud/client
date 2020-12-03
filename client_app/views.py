from django.shortcuts import render

# Create your views here.

from django.conf import settings
from django.core.mail import send_mail, send_mass_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from django.http import (Http404, HttpRequest, HttpResponse,
                         HttpResponseRedirect)
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView,FormView, TemplateView

from .forms import *
from .models import *


class ClientCreateView(FormView):
    model = Client
    form_class = ClientCreateForm
    template_name = 'add_client.html'
    success_url = '/'
    
    def form_valid(self, form):
        if form.is_valid:
            name = form.cleaned_data['client_name']
            email = form.cleaned_data['client_email']
            create_client = Client(client_email = email, client_name = name)
            create_client.save()
        return super().form_valid(form)

class Success(TemplateView):
    template_name = 'success.html'

