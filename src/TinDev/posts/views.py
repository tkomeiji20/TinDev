from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PostForm


# Create your views here.
def create(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'Posts/create.html', {'form': form})
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/dashboard')

    form = PostForm()
    return render(request, 'Posts/create.html', {'form': form})


def index(request):
    return render(request, 'index.html')
