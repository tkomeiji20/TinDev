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
    form = RecruiterForm(request.POST, request.FILES,
                         initial={'user_type': USER_TYPES[0][0]})
    context = {
        "form": RecruiterForm()
    }

    if form.is_valid():
        form.save()

    return render(request, 'user/createrecruiter.html', context)


def new_candidate(request):
    form = CandidateForm(request.POST, request.FILES,
                         initial={'user_type': USER_TYPES[1][0]})
    context = {
        "form": CandidateForm
    }
    if form.is_valid():
        form.save()

    return render(request, 'user/createcandidate.html', context)


def index(request):
    return render(request, 'user/index.html')
