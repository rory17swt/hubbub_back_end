from rest_framework.views import APIView
from rest_framework.response import Response


class EventListCreate(APIView):
    #Index
    def get(self, request):
        return Response('HIT index')

    #Create
    def post(self, request):
        return Response('HIT create')


class EventDetailView(APIView):
    #Show
    def get(self, request, pk):
        return Response('HIT show')
    
    #Update
    def put(self, request, pk):
        return Response('HIT update')
    
    #Delete
    def delete(self, request, pk):
        return Response('HIT delete')