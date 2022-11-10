from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/candidate',views.create_candidate, name='create_candidate'),
    path('create/recruiter',views.create_recruiter, name='create_recruiter'),
    path('login/', views.LoginView, name='login'),
    path('dashboard/',views.candidate_dashboard),
]