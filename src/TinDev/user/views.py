from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User as DjangoUser
from django.contrib.auth import authenticate, login, logout
from django.views import View
from posts.views import getPosts
from .models import User
from .forms import CandidateForm, RecruiterForm, LoginForm
import datetime

# NOTE: See TinDev views login
USER_TYPES = [('Recruiter', 'recruiter'), ('Candidate', 'candidate')]

# https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/




def new_candidate(request):
    '''Handles requests made to create candidates'''
    if request.method == 'POST':
        # Create the candidate
        form = CandidateForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # Check if someone already made the username
            try:
                user = DjangoUser.objects.get(username=username)
                return HttpResponseRedirect('/user/login')
            except ObjectDoesNotExist:
                form.save()

                # Change the user_type to candidate
                user = User.objects.get(username=username)
                print("user: ", user)
                user.user_type = 'candidate'
                user.save()

                logout(request)
                DjangoUser.objects.create_user(
                    username=username, password=user.password)
                return HttpResponseRedirect('/user/login')
        return HttpResponseRedirect('/user/login')
    else:
        # Show the form
        form = CandidateForm()

    return render(request, 'user/create.html', {'form': form, 'user_type': 'candidate'})


def new_recruiter(request):
    '''Handle new recruiter requests'''
    if request.method == 'POST':
        # Attempt to make new recruiter
        form = RecruiterForm(request.POST)
        if form.is_valid():
            # TODO: Check that there is not already a user with the given username
            form.save()
            logout(request)
            DjangoUser.objects.create_user(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            return HttpResponseRedirect('/user/login')
        return HttpResponseRedirect('/user/create/recruiter')
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


def LoginView(request):
    '''Handle Login requests'''
    if request.method == 'GET':
        # Show the form
        form = LoginForm()
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        # Check if the user can login
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Attempt to login the user
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/user/dashboard')
            else:
                # TODO: Add an error message
                return HttpResponseRedirect('/user/login')


# def candidate_dashboard(request):
#     print(request.user.username)
#     user = User.objects.get(username=request.user.username)
#     return render(request, 'user/candidate_dashboard.html', {'user': user})

class UserDashboardView(View):
    '''User Dashboard Logic'''
    filters = ""


    def get(self, request, filters="", more_filters=""):
        '''Handle GET Request Logic'''
        try:
            user = User.objects.get(username=request.user.username)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/user/login')

        print(user.user_type)
        if user.user_type == 'Recruiter':
            posts = getPosts()
            try:
                if filters:
                    if filters == "active":
                        # TODO FIGURE LOGIC OUT
                        today = datetime.datetime.now(datetime.timezone.utc)
                        posts = posts.filter(expiration__gte=today.isoformat())
                    elif filters == "inactive":
                        # TODO FIGURE LOGIC OUT
                        today = datetime.datetime.now(datetime.timezone.utc)
                        posts = posts.filter(expiration__lt=today.isoformat())
                    elif filters == "interest":
                        # TODO FIGURE LOGIC OUT
                        posts = posts
            except AttributeError:
                test = ""
                return render(request, 'user/recruiter_dashboard.html', {'posts': posts, 'user': user, 'test': test,})

            test = ""
            return render(request, 'user/recruiter_dashboard.html', {'posts': posts, 'user': user, 'test': test,})
        else:
            posts = getPosts()
            # try:
            #     print("filters")
            #     if filters:
            #         if filters == "active":
            #             # TODO FIGURE LOGIC OUT
            #             today = datetime.datetime.now(datetime.timezone.utc)
            #             posts = posts.filter(expiration__gte=today.isoformat())
            #         elif filters == "inactive":
            #             # TODO FIGURE LOGIC OUT
            #             today = datetime.datetime.now(datetime.timezone.utc)
            #             posts = posts.filter(expiration__lt=today.isoformat())
            #         elif filters == "interest":
            #             # TODO FIGURE LOGIC OUT
            #             posts = posts
            # except AttributeError:
            print("filters: ", filters)
            if filters:
                if filters == "active":
                    posts = posts.filter(status=True)
                    return render(request, 'Posts/posts_candidate.html', {'posts': posts, 'user': user, })
                if filters == "inactive":
                    posts = posts.filter(status=False)
                    return render(request, 'Posts/posts_candidate.html', {'posts': posts, 'user': user, })
                if filters == "location":
                    posts = posts.filter(location=more_filters)
                    return render(request, 'Posts/posts_candidate.html', {'posts': posts, 'user': user, })
                if filters == "Description":
                    newPosts = list()
                    words = more_filters.split()
                    for word in words:
                        for post in posts:
                            if word in post.description:
                                newPosts.append(post)
                                break
                        # newPosts.append(posts.filter(description.contains(word)))
                    # posts = posts.filter(location=locations)
                    return render(request, 'Posts/posts_candidate.html', {'posts': newPosts, 'user': user, })
                
            return render(request, 'user/candidate_dashboard.html', {'posts': posts, 'user': user, })
        


def LogoutView(request):
    logout(request)
    return HttpResponseRedirect('/')
