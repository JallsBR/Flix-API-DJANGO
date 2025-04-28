from reviews.models import Review
from rest_framework import generics
from reviews.serializer import ReviewSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
