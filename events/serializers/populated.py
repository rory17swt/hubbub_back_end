from .common import EventSerializer
from questions.serializers.common import QuestionSerializer

class PopulatedEventSerializer(EventSerializer):
    questions = QuestionSerializer(many=True)