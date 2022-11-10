from django import forms


class UserForm(forms.Form):
    pass


class CandidateForm(forms.Form):
    name = forms.CharField()
    zipcode = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    profile_bio = forms.TextInput()
    education = forms.CharField()
    github = forms.CharField()
    experience = forms.TextInput()
    skills = forms.TextInput()


class RecruiterForm(forms.Form):
    name = forms.CharField()
    zipcode = forms.IntegerField()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    company = forms.CharField()
