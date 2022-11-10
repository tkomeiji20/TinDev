from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.new_user, name='create'),
    path('createcandidate', views.new_candidate, name='create_candidate'),
    path('createrecruiter', views.new_recruiter, name='create_recruiter')
]
