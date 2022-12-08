from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Post
from django import forms


class PostForm(ModelForm):
    # user_type = forms.CharField(widget=forms.HiddenInput(), initial= USER_TYPES[1][0], max_length=9)
    class Meta:
        model = Post
        # Put Candidate forms
        fields = ['position', 'location', 'skills',
                  'description', 'company', 'expiration', 'type', 'status', ]
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),

            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),

            'expiration': DateTimeInput()
        }
