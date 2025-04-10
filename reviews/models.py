from django.db import models
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator

class Review(models.Model):
    movie = models.ForeignKey(
        Movie, 
        on_delete=models.PROTECT, 
        related_name='reviews'
    )
    comment = models.TextField(blank=True, null=True)
    stars = models.IntegerField(
        validators=[
            MaxValueValidator(5, 'Máximo de 5 estrelas'),
            MinValueValidator(0, 'Mínimo de 0 estrelas'), 
        ]
    )
    
    def __str__(self):
        return str(self.movie)