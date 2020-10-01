from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from members.forms import UserRegForm, ProfileForm, PasswordForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.models import User

class UserRegView(CreateView):
    form_class = UserRegForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class ProfileView(UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordView(PasswordChangeView):
    template_name = 'registration/password.html'
    form_class = PasswordForm
    success_url = reverse_lazy('index')
