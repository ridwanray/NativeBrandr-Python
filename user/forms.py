from django import forms
from .models import Design
from django.contrib.auth.models import User
from registration.forms import RegistrationFormUsernameLowercase, RegistrationFormTermsOfService, RegistrationFormUniqueEmail
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class NewDesign(forms.ModelForm):
		class Meta:
			model = Design
			fields = ['category', 'designImage']
class CustomForm(RegistrationFormUsernameLowercase, RegistrationFormTermsOfService, RegistrationFormUniqueEmail):
	pass