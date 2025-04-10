# Generated by Django 5.2 on 2025-04-10 19:23

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movies', '0002_alter_movie_actors_alter_movie_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True)),
                ('stars', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5, 'Máximo de 5 estrelas'), django.core.validators.MinValueValidator(0, 'Mínimo de 0 estrelas')])),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviews', to='movies.movie')),
            ],
        ),
    ]
