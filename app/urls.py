
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreRetrieveUpdateDestroyView, GenreCreateListView
from actors.views import ActorCreateListView, ActoreRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),    
    
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view() , name='genres-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActoreRetrieveUpdateDestroyView.as_view() , name='actors-detail-view'),
    
    path('movies/', MovieCreateListView.as_view(), name='movies-create-list'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view() , name='movies-detail-view'),
    
    path('reviews/', ReviewCreateListView.as_view(), name='reviews-create-list'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view() , name='reviews-detail-view'),
]
