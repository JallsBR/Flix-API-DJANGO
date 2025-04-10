import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from reviews.models import Review
from rest_framework import generics
from reviews.serializer import ReviewSerializer



class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
