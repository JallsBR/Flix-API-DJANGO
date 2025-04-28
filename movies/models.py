from django.db import models
from genres.models import Genre
from actors.models import Actor

class Movie(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    resume = models.TextField(blank=True, null=True, verbose_name='Resumo')
    release_date = models.DateField(blank=True, null=True, verbose_name='Data de Lançamento')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies', null=True, verbose_name='Gênero')
    actors = models.ManyToManyField(Actor, related_name='movies', verbose_name='Atores')
    
    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
    
    def __str__(self):
        return self.title