from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=150)

	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


	def save(self, commit=True):
		user = super().save(commit=False)

		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()
		return user

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('middlename','date_of_birth', 'twitter_handle', 'fb_handle', 'insta_handle', 'telephone', 'website', 'address1', 'address2', 'city', 'state', 'zipcode', 'about')


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['address1'].widget.attrs.update({'class' : 'form-group', 'placeholder': 'Enter Address Here'})