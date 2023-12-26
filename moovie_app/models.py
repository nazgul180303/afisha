from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=255, null=False)

    # @property
    # def director_count(self):
    #     return self.director_set.count()

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(
        Director, on_delete=models.CASCADE, related_name="director_set"
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")
    rating = models.PositiveIntegerField(
        default=1, choices=[(i, i * "*") for i in range(1, 6)]
    )

    def __str__(self):
        return f"Review for {self.movie.title}"
