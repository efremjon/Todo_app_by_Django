from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import RegstForm
from django.views import generic


class UserRegistrationView(CreateView):
    form_class = RegstForm
    template_name = 'registration/regster.html'
    success_url = reverse_lazy('login')


