from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from .models import User
from .forms import CandidateForm, UserForm, RecruiterForm

# NOTE: See TinDev views login
USER_TYPES = [('Recruiter', 'recruiter'), ('Candidate', 'candidate')]


def new_user(request):
    context = {
    }

    return render(request, 'user/create.html', context)


def new_recruiter(request):
    context = {
        "form": RecruiterForm()
    }
    return render(request, 'user/createrecruiter.html', context)


def new_candidate(request):
    form = CandidateForm(request.POST, request.FILES)
    context = {
        "form": CandidateForm
    }
    if form.is_valid():
        form.save()

    return render(request, 'user/createcandidate.html', context)


def index(request):
    return render(request, 'user/index.html')
