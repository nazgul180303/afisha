from rest_framework import serializers

from .models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    director_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ("id", "name", "director_count")

    def get_director_count(self, obj):
        return obj.director_set.count()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class ReviewMovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ["title", "description", "duration", "reviews", "average_rating"]

    def get_average_rating(self, obj):
        reviews = obj.reviews.all()
        if reviews.count() == 0:
            return 0
        else:
            return round(
                sum([review.rating for review in reviews]) / reviews.count(), 2
            )
