
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import GenreRetrieveUpdateDestroyView, GenreCreateListView
from actors.views import ActorCreateListView, ActoreRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),    
    
    path('genres/', GenreCreateListView.as_view(), name='genres-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view() , name='genres-detail-view'),
    
    path('actors/', ActorCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActoreRetrieveUpdateDestroyView.as_view() , name='actors-detail-view'),
]
