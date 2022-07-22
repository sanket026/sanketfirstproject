from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import contactdata, usersignup,notesdata

class signupform(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class notesdataform(forms.ModelForm):
    class Meta:
        model=notesdata
        fields='__all__'   

class contactform(forms.ModelForm):
    class Meta:
        model=contactdata
        fields='__all__'             