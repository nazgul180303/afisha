"""
URL configuration for afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import moovie_app
from moovie_app.views import DirectoryListAPIView, DirectoryDetailAPIView, MovieListAPIView, MovieDetailAPIView, \
    ReviewListAPIView, ReviewDetailAPIView, ProductReviewListAPIView
from users import views
from users.views import RegistrationAPIView, ConfirmUserAPIView, AuthorizationAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("moovie_app.urls")),
    path('users/registration/', views.registration_api_view),
    path('users/confirm/', views.confirm_user_api_view),
    path('users/authorization/', views.authorization_api_view),
    path('products/directors/', DirectoryListAPIView.as_view()),
    path('products/directors/<int:pk>/', DirectoryDetailAPIView.as_view()),
    path('products/movies/', MovieListAPIView.as_view()),
    path('products/movies/<int:pk>/', MovieDetailAPIView.as_view()),
    path('products/reviews/', ReviewListAPIView.as_view()),
    path('products/reviews/<int:pk>/', ReviewDetailAPIView.as_view()),
    path('products/movies/reviews/', ProductReviewListAPIView.as_view()),
    path('users/registration/', RegistrationAPIView.as_view()),
    path('users/confirm/', ConfirmUserAPIView.as_view()),
    path('users/authorization/', AuthorizationAPIView.as_view()),
]
