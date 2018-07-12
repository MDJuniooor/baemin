from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render, get_object_or_404
from .models import Category, Shop, Review
from .forms import ReviewForm

index = ListView.as_view(model=Category)


category_detail =DetailView.as_view(model=Category)
shop_detail = DetailView.as_view(model=Shop)


class ReviewCreateView(LoginRequiredMixin ,CreateView):
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        self.shop = get_object_or_404(Shop, pk=self.kwargs['pk'])
        review = form.save(commit=False)
        review.shop = self.shop
        review.author = self.request.user
    
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.shop.get_absolute_url()

review_new = ReviewCreateView.as_view()


    
