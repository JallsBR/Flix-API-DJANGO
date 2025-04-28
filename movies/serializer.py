from datetime import date
from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg, Count


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    

    def get_rate(self, obj):
        stats = obj.reviews.aggregate(
            media=Avg('stars'),
            reviews=Count('id')
        )
        return {
            "média": round(stats['media'], 1) if stats['media'] is not None else 0,
            "reviews": stats['reviews']
        }
        
    class Meta:
        model = Movie
        fields = '__all__'
        


        def validate_release_date(self, value):
            if value > date.today():
                raise serializers.ValidationError("A data de lancamento nao pode ser maior que a data atual")
            return value
        
        def validate_resume(self, value):
            if len(value) > 200:
                raise serializers.ValidationError("O resumo nao pode ser maior que 200 caracteres")
            return value
        
        def validate_title(self, value):
            if len(value) < 3:
                raise serializers.ValidationError("O titulo nao pode ter menos de 3 caracteres")
            return value