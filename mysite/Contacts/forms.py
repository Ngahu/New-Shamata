from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,help_text='Enter your Name Here, 100 characters max ') 
    phonenumber = PhoneNumberField(required=True,help_text='Enter your Phone Number Here Starting With Country Code')
    email = forms.EmailField(required=True,help_text='Enter your Email Adress Here ')
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True,widget=forms.Textarea,help_text='Enter your Comment Here')