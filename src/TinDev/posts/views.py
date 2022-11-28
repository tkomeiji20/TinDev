from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from user.models import User
from .forms import PostForm
from .models import Post


# Create your views here.
def get_user_permisions(request):
    '''Returns whether user is a recruiter or a candidate'''
    try:
        user = User.objects.get(username=request.user.username)
    except ObjectDoesNotExist:
        return False
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
