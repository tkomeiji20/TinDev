from django.urls import path
from .views import CreateOffer

# Patterns
urlpatterns = [
    path('<int:post_id>/<int:candidate_id>/',CreateOffer.as_view()),
]