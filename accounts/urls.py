from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.urls import path, include, reverse_lazy
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('login/',login, name='login', kwargs={
        'template_name': 'accounts/login_form.html',
    }),
    path('logout/', logout, name='logout', kwargs={
        'template_name': 'accounts/logout_form.html',
        'next_page': reverse_lazy('root'),
    }),
    path('profile/', views.profile, name='profile'),
]
