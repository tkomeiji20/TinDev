from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import User
from .forms import CandidateForm, UserForm, RecruiterForm

# NOTE: See TinDev views login
USER_TYPES = [('Recruiter', 'recruiter'), ('Candidate', 'candidate')]


def new_user(request):
    context = {
        "form": UserForm()
    }

    return render(request, 'user/create.html', context)


def new_recruiter(request):
    context = {
        "form": RecruiterForm()
    }
    return render(request, 'user/createrecruiter.html', context)


def new_candidate(request):
    context = {
        "form": CandidateForm()
    }
    print('tets')
    if request.method == 'POST':
        print('test')
        form = CandidateForm(request.POST)
        if form.is_valid():
            name = forms.cleaned_data['name']
            zipcode = forms.cleaned_data['zipcode']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            profile_bio = forms.cleaned_data['profile_bio']
            education = forms.cleaned_data['education']
            github = forms.cleaned_data['github']
            experience = forms.cleaned_data['experience']
            skills = forms.cleaned_data['skills']
            user = User(
                name=name, zipcode=zipcode, username=username, password=password,
                profile_bio=profile_bio, education=education, github=github, experience=experience,
                skills=skills, user=user, user_type=USER_TYPES[1], company='')
            user.save()
    else:
        print("another tets")
    return render(request, 'user/createcandidate.html', context)


def index(request):
    return render(request, 'user/index.html')
