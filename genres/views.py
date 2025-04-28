
from genres.models import Genre
from rest_framework import generics
from genres.serializer import GenreSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly



class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    
    
class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

'''
@csrf_exempt
def genre_create_list_view(request):
    if request.method == 'GET':
        genres = Genre.objects.all()

        #data = []
        #for genre in genres:
        #    data.append({
        #        'id': genre.id,
        #        'name': genre.name 
        #    }) 
               
        #list compreension
        data = [{'id': genre.id, 'name': genre.name} for genre in genres] 
        return JsonResponse(data , safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)


    
@csrf_exempt
def genre_detail_view(request, pk):
    # genre = Genre.objects.get(pk=pk)
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'GET':
        data = { 'id': genre.id, 'name': genre.name}
        return JsonResponse(data, status=200)
    elif request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        genre.name = data['name']
        genre.save()
        return JsonResponse({'message': 'Gênero alterado com sucesso'}, status=201)
    elif request.method == 'DELETE':
        genre.delete()
        return JsonResponse({'message': 'Gênero deletado com sucesso'}, status=200)
    
'''