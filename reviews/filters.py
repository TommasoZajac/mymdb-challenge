from rest_framework import generics
from django_filters import rest_framework as filters
from reviews.models import Review


class FilmReviewFilter(filters.FilterSet):
    

    class Meta:
        model = Review
        fields = ['object_id']

