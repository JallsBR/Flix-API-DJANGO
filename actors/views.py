from actors.models import Actor
from rest_framework import generics
from actors.serializer import ActorSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    
    
class ActoreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer



