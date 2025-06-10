from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Question
from .serializers.populated import populatedQuestionSerializer
from rest_framework.permissions import BasePermission, IsAuthenticatedOrReadOnly


class IsEventOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return obj.event.owner == request.user


class QuestionListView(ListCreateAPIView):
    serializer_class = populatedQuestionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        event_id = self.kwargs.get('event_id')
        return Question.objects.filter(event_id=event_id).order_by('created_at')

    def perform_create(self, serializer):
        event_id = self.kwargs.get('event_id')
        serializer.save(event_id=event_id, owner=self.request.user)


class QuestionDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = populatedQuestionSerializer
    permission_classes = [IsEventOwnerOrReadOnly]
