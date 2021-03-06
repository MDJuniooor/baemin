from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.conf import settings
from django.db import models
from jsonfield import JSONField
from .payment import BaseOrder
import json

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:category_detail', args=[self.pk])


class Shop(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    latlng = models.CharField(max_length=100, blank=True)
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField(blank=True) # Postgre의 Jsonb 타입과 다르다
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:shop_detail', args=[self.pk])


    @property
    def address(self):
        print(self.meta.get('address'))
        return self.meta.get('address')

class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True)
    photo = models.ImageField(blank=True, null=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], default=1, null=True,blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    meta = JSONField(blank=True) # Postgre의 Jsonb 타입과 다르다
    
    def __str__(self):
        return self.name

class Review(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True, null=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(
        1), MaxValueValidator(5)], null=True, blank=True)
    message = models.TextField(null=True)

    class Meta:
        ordering = ['-id',]

    def __str__(self):
        return self.message


class Order(BaseOrder):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # amount
    @property
    def amount(self):
        return self.quantity * self.item.amount
