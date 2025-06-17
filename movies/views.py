from django.shortcuts import render
from django.views import generic
from movies.models import Movie
from movies.models import Character
from rest_framework import viewsets
from movies.serializers import MovieSerializer

class MovieListView(generic.ListView):
    model=Movie
    template_name="movies/movielist.html"
    
class CharacterListView(generic.ListView):
    model=Character
    template_name="movies/characterlist.html"

class MovieViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly]
    ordering = ['id']