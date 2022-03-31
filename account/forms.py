from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.urls import reverse

class RegstForm(UserCreationForm):
    first_name = forms.CharField(label='first_name', min_length=5, max_length=150)  
    last_name = forms.CharField(label='last_name', min_length=5, max_length=150)
    email = forms.EmailField(label='email')
    class Meta:
        model=User
        def get_absolute_url(sefl):
            return reverse ('home')
        fields = ['first_name','last_name','email','username','password1','password2']
