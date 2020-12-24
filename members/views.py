from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignupForm


class UserSignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('login')
