from django import forms
from . import models


class TypeModelForm(forms.ModelForm):
    class Meta:
        model = models.Type
        fields = [
            "category", 
            "name", 
            "description", 
            "picture"
        ]
        
class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "name", 
            "description", 
            "picture"
        ]
        
    