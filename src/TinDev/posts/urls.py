from django.urls import path
from . import views
from .views import UpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('update/<int:id>/', UpdateView.as_view())
]