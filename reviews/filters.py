from rest_framework import generics
from django_filters import rest_framework as filters
from reviews.models import Review
from django.contrib.contenttypes.models import ContentType


class ReviewFilter(filters.FilterSet):
    #passa content type
    content_type = filters.ModelChoiceFilter(
        queryset = ContentType.objects.all(),
        required= True
    )
    class Meta:
        model = Review
        fields = ['content_type','object_id']#aggiungi content type


