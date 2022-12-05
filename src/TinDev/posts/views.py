from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from user.models import User
from django.views import View
from .forms import PostForm
from .models import Post


# Create your views here.
def get_user_permisions(request):
    '''Returns whether user is a recruiter or a candidate'''
    try:
        user = User.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        return ""
    return user.user_type

def create(request):
    # Render the dashboard or create the post depending on request type
    if request.method == 'GET':
        # Validate the user is a recruiter
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')

        # Render the template
        form = PostForm()
        return render(request, 'Posts/create.html', {'form': form})

    elif request.method == 'POST':
        form = PostForm(request.POST)
        # TODO: Add a check to see valid permissions
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')
        # Check: https://docs.djangoproject.com/en/4.1/topics/auth/default/
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/dashboard')

    form = PostForm()
    return render(request, 'Posts/create.html', {'form': form})

class UpdateView(View):
    '''Handle updates to the Posts'''
    def get(self, request, id=-1):
        '''Handle the GET requests'''
        # Validate User permissions
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')
        # Validate the post
        if id < 0:
            return HttpResponseRedirect('/posts/create')

        # Query Object
        try:
            update_post = Post.objects.get(pk=id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/posts/create')

        # Render UI for updating posts
        form = PostForm(instance=update_post)
        return render(request, 'Posts/create.html', {'form': form})

    def post(self,request, id=-1):
        '''Handle POST requests'''
        # Validate User permissions
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')
        # Verify the post exists
        if id < 0:
            return HttpResponseRedirect('/posts/create')

        # Query Object
        try:
            update_post = Post.objects.get(pk=id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/posts/create')

        # Update the object
        form = PostForm(request.POST, instance=update_post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/user/dashboard')


class DeleteView(View):
    '''Deletes a given post'''
    def get(self, request, id =-1):
        '''Delete Post from database'''
        # Validate User permissions
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')

        # Verify the post exists
        if id < 0:
            return HttpResponseRedirect('/posts/create')

        # Query Object
        try:
            update_post = Post.objects.get(pk=id)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/posts/create')

        # TODO: Verify user is connected to post

        # Delete the post
        update_post.delete()
        return HttpResponseRedirect('/user/dashboard/')


def getPosts(query=-1):
    '''Gets specific post id, else returns all posts'''
    if query == -1:
        posts = Post.objects.all()
        return posts

    try:
        return Post.objects.get(query)
    except ObjectDoesNotExist:
        return None


'''Handles interest to the Posts from the Users'''
def Interest(request, id_post=-1, id_user=-1, check = None):
    
    '''Handle the GET requests'''
    # Validate the post
    if id_post < 0:
        return HttpResponseRedirect('/user/candidate_dashboard.html')

    # Validate the user and user permissions
    if id_user < 0:
        return HttpResponseRedirect('/user/candidate_dashboard.html')
    user = User.objects.get(pk=id_user)
    try:
        if user.user_type != "candidate":
            print(user.user_type)
            return HttpResponseRedirect('/user/login')
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/user/login')
    # Query Object
    try:
        interest_post = Post.objects.get(pk=id_post)
        if check != None:
            if check == False:
                interest_post.interest.delete(user.pk)
            else:
                interest_post.interest.add(user.pk)
            interest_post.save()
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/user/candidate_dashboard.html')
    
    return HttpResponseRedirect('/user/dashboard/interest/')

def index(request):
    return render(request, 'index.html')
