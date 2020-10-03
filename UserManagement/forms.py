from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ('name','Picture_Picture','Phone')