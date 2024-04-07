from django import forms
from django.forms import ModelForm
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        
class Orders_Form(ModelForm):
    class Meta:
        model=Orders
        #fields='__all__'
        fields=['customer_reference','product_reference','order_number','order_date','quantity']


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['department', 'area', 'title', 'short_text_field', 'brief_description', 'image']
