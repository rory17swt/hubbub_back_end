from rest_framework.serializers import ModelSerializer
from ..models import User
from events.serializers.common import EventSerializer

class ProfileSerializer(ModelSerializer):
    events = EventSerializer(many=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'events', 'bio']