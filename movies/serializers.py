from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = round(obj.reviews.aggregate(Avg('stars'))['stars__avg'], 1)

        if rate:
            return rate
        
        return None

    def validate_release_date(self, value):
        if value.year < 1950:
            raise serializers.ValidationError('Ano de lançamento não pode ser anterior a 1950')
        return value
    
    def validate_resume(self, value):
        if len(value) > 40:
            raise serializers.ValidationError(f'Tamanho do campo excede o limite de 40 caraceteres. Caracteres incluídos: {len(value)}')
        return value
    
class MovieStatsSerializer(serializers.Serializer):
    total_movies = serializers.IntegerField()
    movies_by_genre = serializers.ListField()
    total_reviews = serializers.IntegerField()
    average_stars = serializers.FloatField()
