# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import User_registration


class User_RegistrationForm(ModelForm):

    class Meta:
    	model = User_registration
    	# fields = '__all__'
    	fields = ['image', 'first_name', 'last_name', 'email_id', 'password']
