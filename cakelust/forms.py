from django.forms import ModelForm
from django import forms
from .models import *


class reviewsForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name','custreview']
        widgets={
            'custreview' : forms.Textarea(attrs={
                'placeholder':'How was your experience?',
                'resize': 'both',
                'overflow': 'auto',
            }),
            'name' : forms.TextInput(attrs={
                'placeholder':'Type in your name',
                'resize': 'both',
            })
        }