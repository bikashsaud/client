from django.urls import path, include
from django.contrib import admin
from .views import *
# import app.views
admin.autodiscover()

app_name = 'client_app'

urlpatterns = [
    path('', Success.as_view(), name ='success'),

    path('client/create/', ClientCreateView.as_view(), name ='client_create'),
]

