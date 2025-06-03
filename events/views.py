from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Event
from .serializers.common import EventSerializer


class EventListCreate(APIView):
    #Index
    def get(self, request):
        events = Event.objects.all()
        serialized_events = EventSerializer(events, many=True)
        return Response(serialized_events.data)

    #Create
    def post(self, request):
        request.data['owner'] = request.user.id
        serialized_event = EventSerializer(data=request.data)
        serialized_event.is_valid(raise_exception=True)
        serialized_event.save()
        return Response(serialized_event.data, 201)


class EventDetailView(APIView):
    #Show
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        serialized_event = EventSerializer(event)
        return Response(serialized_event.data)
    
    #Update
    def put(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        self.check_object_permissions(request, event)
        serilized_event = EventSerializer(event, data=request.data, partial=True)
        serilized_event.is_valid(raise_exception=True)
        serilized_event.save()
        return Response(serilized_event.data)
    
    #Delete
    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        self.check_object_permissions(request, event)
        event.delete()
        return Response("Event Deleted", status=204)