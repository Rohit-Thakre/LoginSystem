from django import forms
from . models import cUser
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm): 
    class Meta: 
        model = cUser
        fields = [ 'profile_pic','first_name', 'last_name', 'email']



class LoginForm(forms.Form):
    username =  forms.CharField(max_length=150, required=True)
    password = forms.CharField(required = True)