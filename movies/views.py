from django.shortcuts import render
from django.views import generic
from movies.models import Movie
from movies.models import Character
from rest_framework import viewsets
from movies.serializers import MovieSerializer,CharacterSerializer
from django.db.models.functions import Concat
from django.db.models import CharField, Value

class MovieListView(generic.ListView):
    model=Movie
    template_name="movies/movielist.html"
    
class CharacterListView(generic.ListView):
    model=Character
    template_name="movies/characterlist.html"

class MovieViewSet(viewsets.ModelViewSet):
    
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    ordering = ['id']

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    ordering = ['id']

    def get_queryset(self):
        qs= super().get_queryset()
        qs = qs.annotate(
            person_name=Concat("person__first_name",Value(" ") ,"person__last_name",
                               output_field = CharField())
        )
        return qs