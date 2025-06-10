from .common import QuestionSerializer
from users.serializers.common import UsernameSerializer


class populatedQuestionSerializer(QuestionSerializer):
    owner = UsernameSerializer()
