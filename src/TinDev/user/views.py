from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import User

# NOTE: See TinDev views login


# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
class CandidateForm(forms.ModelForm):
    class Meta:
        model = User
        # Put Candidate forms
        fields =['name', 'profile_bio', 'zipcode', 'skills', 'github',
        'experience', 'education', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

def new_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)
        form.save()
        # if form.is_valid():
        return HttpResponseRedirect('/')
    else:
        form = CandidateForm()

    return render(request, 'user/create.html', {'form': form, 'user_type': 'candidate'})

class RecruiterForm(forms.ModelForm):
    class Meta:
        model = User
        # Put Candidate forms
        fields =['name', 'company', 'zipcode', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

def new_recruiter(request):
    if request.method == 'POST':
        form = RecruiterForm(request.POST)
        form.save()
        # if form.is_valid():
        return HttpResponseRedirect('/')
    else:
        form = RecruiterForm()

    return render(request, 'user/create.html', {'form': form, 'user_type': 'recruiter'})

# Create your views here.
def create(request):
    return new_candidate(request)

def index(request):
    return render(request, 'user/index.html')