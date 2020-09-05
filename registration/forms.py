# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

from django.forms import ModelForm
from .models import User_registration


class User_RegistrationForm(ModelForm):
	first_name = forms.CharField()
	last_name = forms.CharField()
	image		= models.ImageField(upload_to=user_image)
	age 		= models.IntegerField()
	unique_id 	= get_random_string()											# models.AutoField( default=True)
	email_id	= models.EmailField()
	password 	= models.CharField()
	password_verify = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Verify password'}), label="")

	def clean_password(self):
        # print self.cleaned_data
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password_verify')
        if not password2:
            raise forms.ValidationError("You must confirm your password")
        if password1 != password2:
        raise forms.ValidationError(_('Your passwords do not match'), code='invalid') 
        return password2


    class Meta:
    	model = User_registration
    	# fields = '__all__'
    	fields = ['image', 'first_name', 'last_name', 'email_id', 'password']
