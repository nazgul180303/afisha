from django.db.models import OuterRef, Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .models import Director, Movie, Review
from .serializers import (
    DirectorSerializer,
    MovieSerializer,
    ReviewSerializer,
    ReviewMovieSerializer,
)


@api_view(["GET", 'POST'])
def director_list(request):
    if request.method == "GET":
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = DirectorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", 'PUT', 'DELETE'])
def director_detail(request, id):
    try:
        post = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404)
    if request.method == "GET":
        director = get_object_or_404(Director, id=id)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = DirectorSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=404)


@api_view(["GET", 'POST'])
def movie_list(request):
    if request.method == "GET":
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET"])
def movie_detail(request, id):
    try:
        post = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(status=404)
    if request.method == "GET":
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MovieSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=404)


@api_view(["GET", 'POST'])
def review_list(request):
    if request.method == "GET":
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(["GET", 'PUT', 'DELETE'])
def review_detail(request, id):
    try:
        post = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(status=404)
    if request.method == "GET":
        review = get_object_or_404(Review, id=id)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = ReviewSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == "DELETE":
        post.delete()
        return Response(status=404)


@api_view(["GET"])
def review_movie_list(request):
    reviews = Movie.objects.all()
    serializer = ReviewMovieSerializer(reviews, many=True)
    return Response(serializer.data)



class DirectoryListAPIView(ListCreateAPIView):
    queryset = Director.objects.prefetch_related('directors').all()
    serializer_class = DirectorSerializer


class DirectoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewListAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ProductReviewListAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = ReviewMovieSerializer