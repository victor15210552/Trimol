from django import forms
from Aplicacion.models import Hospital, Especialidad, Sector, Estado
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
    	model = User
    	fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class Hospital_form(forms.ModelForm):
	class Meta:
		model=Hospital
		fields='__all__'

class Especialidad_form(forms.ModelForm):
	class Meta:
		model=Especialidad
		fields='__all__'

class Estado_form(forms.ModelForm):
	class Meta:
		model=Estado
		fields='__all__'

class Sector_form(forms.ModelForm):
	class Meta:
		model=Sector
		fields='__all__'