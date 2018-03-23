from django import forms
from .models import *

class Site_Form(forms.ModelForm):

    class Meta:
        model = Site
        exclude = [""]
