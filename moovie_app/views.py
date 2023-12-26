from django.db.models import OuterRef, Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Director, Movie, Review
from .serializers import (
    DirectorSerializer,
    MovieSerializer,
    ReviewSerializer,
    ReviewMovieSerializer,
)


@api_view(["GET"])
def director_list(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def director_detail(request, id):
    director = get_object_or_404(Director, id=id)
    serializer = DirectorSerializer(director)
    return Response(serializer.data)


@api_view(["GET"])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(["GET"])
def review_list(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def review_detail(request, id):
    review = get_object_or_404(Review, id=id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(["GET"])
def review_movie_list(request):
    reviews = Movie.objects.all()
    serializer = ReviewMovieSerializer(reviews, many=True)
    return Response(serializer.data)
