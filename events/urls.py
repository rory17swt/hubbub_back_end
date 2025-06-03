from django.urls import path 

from .views import EventListCreate, EventDetailView


urlpatterns = [
    path('', EventListCreate.as_view()),
    path('<int:pk>/', EventDetailView.as_view())
]
