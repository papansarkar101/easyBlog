from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignupForm
from .models import Profile


class UserSignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('login')

class UserProfileView(CreateView):
    model = Profile
    template_name = 'registration/profile.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        user = Profile.objects.all()
        context = super(UserProfileView, self).get_context_data(*args, **kwargs)
        return context
