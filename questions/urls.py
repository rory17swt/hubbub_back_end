from django.urls import path
from .views import QestionListView, QuestionDetailView

urlpatterns = [
    path('', QestionListView.as_view()),
    path('<int:pk>/', QuestionDetailView.as_view())
]