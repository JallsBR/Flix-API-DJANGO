
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from genres.views import genre_create_list_view, genre_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('genres/', genre_create_list_view, name='genres-create-list'),
    path('genres/<int:pk>/', genre_detail_view , name='genres-detail-view'),
]
