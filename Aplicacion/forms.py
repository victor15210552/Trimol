from django import forms
from Aplicacion.models import Hospital, Sector, Estado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)



class SignUpForm(UserCreationForm):
	email = forms.EmailField()
	image = forms.ImageField()
	Direccion=forms.CharField(max_length=30)

class Hospital_form(forms.ModelForm):
	class Meta:
		model=Hospital
		fields='__all__'



class Estado_form(forms.ModelForm):
	class Meta:
		model=Estado
		fields='__all__'

class Sector_form(forms.ModelForm):
	class Meta:
		model=Sector
		fields='__all__'
