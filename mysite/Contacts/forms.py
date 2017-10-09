from django import forms
from phonenumber_field.modelfields import PhoneNumberField


class contactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100,help_text='Enter your Name Here, 100 characters max ') 
   # phonenumber = PhoneNumberField()
    email = forms.EmailField(required=True,help_text='Enter your Email Adress Here ')
    message = forms.CharField(required=True,widget=forms.Textarea,help_text='Enter your Message Here')