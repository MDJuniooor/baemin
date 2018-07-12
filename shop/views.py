from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import Category, Shop, Review
from .forms import ReviewForm

index = ListView.as_view(model=Category)


category_detail =DetailView.as_view(model=Category)
shop_detail = DetailView.as_view(model=Shop)

review_new = CreateView.as_view(model=Review, form_class=ReviewForm)