from django.db import models
from genres.models import Genre
from actors.models import Actor

class Movie(models.Model):
    title = models.CharField(max_length=200)
    resume = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name='movies', null=True)
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    def __str__(self):
        return self.title