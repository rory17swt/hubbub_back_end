from .common import EventSerializer
from users.serializers.common import UsernameSerializer
from questions.serializers.common import QuestionSerializer


class PopulatedEventSerializer(EventSerializer):
    owner = UsernameSerializer()
    questions = QuestionSerializer(many=True)