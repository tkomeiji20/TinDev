from django.urls import path
from . import views
from .views import UpdateView, DeleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:id>/', UpdateView.as_view()),
    path('delete/<int:id>/', DeleteView.as_view()),
    path('uninterest/<int:id_post>/', views.Uninterest),
    path('interest/<int:id_post>/', views.Interest, name='Interest'),
]