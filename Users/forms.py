from django import forms
from .models import Users
from django.forms import ModelForm
# from django.contrib.auth.models import User


class UserRegisterForm(ModelForm):
	first_name=forms.CharField(label='First name', max_length=100)
	last_name=forms.CharField(label='Last name', max_length=100)
	email = forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput())
	phone = forms.RegexField(regex=r'^01[0-2]{1}[0-9]{8}')
	Img=forms.ImageField(required=False)
	class Meta:
		model = Users
		fields = ['first_name', 'last_name', 'email','password','phone','Img']

class UserLoginForm(ModelForm):
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = Users
		fields = ['email', 'password']


