from . models import collection
from django import forms

class ModeForm(forms.ModelForm):
    class Meta:
        model=collection
        fields=['image','name']