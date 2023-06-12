from django import forms
from . import models


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = models.Type
        fields = [
            "name",
            "item_number", 
            "picture",
            "description",
            "price",
            "category",
            "type",
            "country",
            "brand",
            "enable",
            "count",
            "search_terms",
            "discount"


        ]
    
    
    