from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'shop'



urlpatterns = [
    path('',views.index, name = 'index'),
    path('category/<pk>', views.category_detail, name='category_detail')
]
