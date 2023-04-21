from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorMovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', )


class ActorSerializer(serializers.ModelSerializer):
    movie_set = ActorMovieSerializer(many=True, read_only=True)
    
    class Meta:
        model = Actor
        fields = ['id', 'name', 'movie_title']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['movies'] = rep.pop('movie_set', [])
        return rep


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'overview', 'release_date', 'poster_path', 'actors']


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('title', 'overview')


class ActorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ('id', 'name')


class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('title', 'content')


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()    
    class Meta:
        model = Review
        fields = ('id', 'movie', 'title', 'content', )