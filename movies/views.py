
from movies.models import Movie
from rest_framework import generics
from movies.serializer import MovieSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly





class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    
    
class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
