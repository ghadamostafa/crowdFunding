from django import forms
# from .models import Users
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	phone = forms.RegexField(regex=r'^01[0-2]{1}[0-9]{8}')
	Img=forms.ImageField(required=False)
	class Meta:
		model = User
		fields = ['username','first_name', 'last_name', 'email','password1', 'password2','phone','Img']

# class UserLoginForm(ModelForm):
# 	email = forms.EmailField()
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	class Meta:
# 		model = User
# 		fields = ['email', 'password']


