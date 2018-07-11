from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Category


index = ListView.as_view(model=Category)


category_detail =DetailView.as_view(model=Category)