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
        if get_user_permisions(request) != "Recruiter":
            return HttpResponseRedirect('/user/login')
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

def getPosts(query=-1):
    '''Gets specific post id, else returns all posts'''
    if query == -1:
        posts = Post.objects.all()
        return posts

    try:
        return Post.objects.get(query)
    except ObjectDoesNotExist:
        return None



def index(request):
    return render(request, 'index.html')
