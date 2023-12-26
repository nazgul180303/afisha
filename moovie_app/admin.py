from django.contrib import admin

# Register your models here

from .models import Director, Review, Movie


admin.site.register(Director)
admin.site.register(Review)
admin.site.register(Movie)
