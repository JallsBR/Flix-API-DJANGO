from django.http import JsonResponse
from genres.models import Genre

def genre_view(request):
    genres = Genre.objects.all()
    '''data = []
    for genre in genres:
        data.append({
            'id': genre.id,
            'name': genre.name 
        }) 
    '''       
    #list compreension
    data = [{'id': genre.id, 'name': genre.name} for genre in genres] 
    return JsonResponse(data , safe=False)
    