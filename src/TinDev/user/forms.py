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
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'profile_bio': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.TextInput(attrs={'class': 'form-control'}),
            'github': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            # 'user_type': forms.HiddenInput(),
        }


class RecruiterForm(forms.ModelForm):
    '''Recruiter Signup Information'''
    class Meta:
        model = User
        # Put Candidate forms
        fields = ['name', 'company', 'zipcode', 'username', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
