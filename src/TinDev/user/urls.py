from django.urls import path
from . import views
from .views import UserDashboardView

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('create/candidate',views.create_candidate, name='create_candidate'),
    path('create/recruiter',views.create_recruiter, name='create_recruiter'),
    path('login/', views.LoginView, name='login'),
    path('dashboard/', UserDashboardView.as_view()),
    path('dashboard/<str:filters>/<str:more_filters>', UserDashboardView.as_view()),
    path('logout/', views.LogoutView),
]