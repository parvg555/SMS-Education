from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class newclass(forms.Form):
    Class_Name = forms.CharField(help_text = "Enter name of classroom")
    Subject = forms.CharField(help_text = "Enter Subject")
    