from django.urls import path
from .views import CreateOffer, Decision

# Patterns
urlpatterns = [
    path('<int:post_id>/<int:candidate_id>/',CreateOffer.as_view()),
    path('decision/<int:offer_id>/<str:response_type>/', Decision.as_view()),
]