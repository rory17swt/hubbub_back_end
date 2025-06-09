from django.urls import path 

from .views import EventListCreate, EventDetailView
from questions.views import QuestionListView


urlpatterns = [
    path('', EventListCreate.as_view()),
    path('<int:pk>/', EventDetailView.as_view()),
    path('<int:event_id>/questions/', QuestionListView.as_view())
]
