from django.forms import ModelForm
from django import forms
from .models import User


class CandidateForm(forms.ModelForm):
    # user_type = forms.CharField(widget=forms.HiddenInput(), initial= USER_TYPES[1][0], max_length=9)
    class Meta:
        model = User
        # Put Candidate forms
        fields = ['name', 'profile_bio', 'zipcode', 'skills', 'github',
                  'experience', 'education', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            # 'user_type': forms.HiddenInput(),
        }


class RecruiterForm(forms.ModelForm):
    '''Recruiter Signup Information'''
    class Meta:
        model = User
        # Put Candidate forms
        fields = ['name', 'company', 'zipcode', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
