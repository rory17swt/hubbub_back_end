from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .models import Question
from .serializers.common import QuestionSerializer
from utils.permissions import IsOwnerOrReadOnly


class QestionListView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsOwnerOrReadOnly]