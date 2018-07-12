from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
User = get_user_model()

signup = CreateView.as_view(model=User, form_class=UserCreationForm,
    template_name='accounts/signup_form.html',
    success_url= reverse_lazy('root'))

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')
