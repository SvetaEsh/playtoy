from django import forms
from . import models
from django.core.validators import RegexValidator

class CreateOrderForm(forms.Form):
        
        adress=forms.CharField(
                required=True,
                widget=forms.Textarea
        )
        phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
        telefon=forms.CharField(validators = [phoneNumberRegex], max_length = 13)
    
        

    
