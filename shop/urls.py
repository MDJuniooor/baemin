from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'shop'



urlpatterns = [
    path('',views.index, name = 'index'),
    path('shop/<pk>/', views.shop_detail, name='shop_detail'),
    path('shop/<pk>/review/new/', views.review_new, name="review_new"),
    path('<shop_pk>/order/new/',views.order_new, name='order_new'),
    path('<shop_pk>/order/<merchant_uid>/pay/', views.order_pay, name='order_pay'), 
    path('category/<pk>', views.category_detail, name='category_detail'),

]
