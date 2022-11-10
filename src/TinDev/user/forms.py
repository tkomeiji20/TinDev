
from django.forms import ModelForm
from django import forms
from .models import User


class UserForm(ModelForm):
    pass


class CandidateForm(ModelForm):
    name = forms.CharField()
    zipcode = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    profile_bio = forms.TextInput()
    education = forms.CharField()
    github = forms.CharField()
    experience = forms.TextInput()
    skills = forms.TextInput()

    class Meta:
        model = User
        fields = [
            'name', 'zipcode', 'username', 'password', 'profile_bio', 'education', 'github', 'experience', 'skills'
        ]
        exclude = ['company', 'user_type']


class RecruiterForm(ModelForm):
    name = forms.CharField()
    zipcode = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    company = forms.CharField()

    class Meta:
        model = User
        field = [
            'name', 'zipcode', 'username', 'password', 'company'
        ]
        exclude = ['profile_bio', 'education',
                   'github', 'experience', 'skills', 'user_type']
