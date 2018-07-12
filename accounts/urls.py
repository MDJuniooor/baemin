from django.contrib import admin
from django.contrib.auth.views import login
from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/',login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
        
    }),
]
