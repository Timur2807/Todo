from django import forms
from .models import ToDO

class ToDOForm(forms.ModelForm):
    class Meta:
        model = ToDO
        fields = 'title', 'memo', 'important'
