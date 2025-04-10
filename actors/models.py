from django.db import models

NATIONALITY_CHOISES = (
    ('BR', 'Brazilian'),
    ('US', 'American'),
    ('MX', 'Mexican'),
    ('AR', 'Argentinian'),
    ('CO', 'Colombian'),
    ('VE', 'Venezuelan'),
    ('EC', 'Ecuadorian'),
    ('CL', 'Chilean')
)

class Actor(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(null=True, blank=True, choices=NATIONALITY_CHOISES, max_length=100)
    birthday = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.name

