from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

class SignUpModelForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name','email']
		#exclude = ['email'] use sparingly
	