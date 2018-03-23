from django import forms
from .models import *

class Customer_Form(forms.ModelForm):

    class Meta:
        model = Customer
        exclude = [""]
