from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignupForm, EditPersonalInfoForm, PasswordChangingForm, ProfilePageForm
from home.models import Profile


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    form_class = ProfilePageForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = "registration/edit_profile.html"

    success_url = reverse_lazy('home')


class UserSignupView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'

    success_url = reverse_lazy('login')

class UserProfileView(generic.UpdateView):
    form_class = EditPersonalInfoForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')
