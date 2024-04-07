#--------------------Video 11
from django.forms import ModelForm
from .models import *

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class ProductForm2(ModelForm):
    class Meta:
        model = Product
        fields = []