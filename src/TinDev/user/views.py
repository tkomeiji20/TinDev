from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate, login
from .models import User

# NOTE: See TinDev views login
USER_TYPES = [('Recruiter', 'recruiter'), ('Candidate', 'candidate')]

# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/
class CandidateForm(forms.ModelForm):
    # user_type = forms.CharField(widget=forms.HiddenInput(), initial= USER_TYPES[1][0], max_length=9)
    class Meta:
        model = User
        # Put Candidate forms
        fields =['name', 'profile_bio', 'zipcode', 'skills', 'github',
        'experience', 'education', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            # 'user_type': forms.HiddenInput(),
        }

def new_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            # Check if someone already made the username
            try:
                user = DjangoUser.objects.get(username=username)
                return HttpResponseRedirect('/')
            except ObjectDoesNotExist:
                form.save()

                # Change the user_type to candidate
                user = User.objects.get(username=username)
                user.user_type = 'candidate'
                user.save()

                DjangoUser.objects.create_user(username=username, password=user.password)
                response = HttpResponseRedirect('/user/dashboard', headers={'pk':user.id})

                return response



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
        if form.is_valid():
            form.save()
            User.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            return HttpResponseRedirect('/')
        return HttpResponseRedirect('')
    else:
        form = RecruiterForm()

    return render(request, 'user/create.html', {'form': form, 'user_type': 'recruiter'})

# Create your views here.
def create(request):
    return new_candidate(request)

def create_candidate(request):
    return new_candidate(request)

def create_recruiter(request):
    return new_recruiter(request)

def index(request):
    return render(request, 'user/index.html')

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }


def LoginView(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/dashboard')
            else:
                return render(request, 'user/login.html')

            # user = User.objects.get(username=username)
            # if not user or user.password != password:
            #     # Probably should render error message
            #     return render(request, 'user/login.html', {'form': form})
            # else:
            #     return HttpResponseRedirect('/user/dashboard', headers={'pk':user.id})

def candidate_dashboard(request):
    user = User.objects.get(username=request.user.username)
    return render(request, 'user/candidate_dashboard.html', {'user': user})