from django import forms
from .models import *

class Team_Form(forms.ModelForm):

    class Meta:
        model = Team
        exclude = [""]
