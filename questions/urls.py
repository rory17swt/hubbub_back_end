from django.urls import path
from .views import QuestionDetailView

urlpatterns = [
    path('<int:pk>/', QuestionDetailView.as_view())
]