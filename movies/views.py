from django.shortcuts import render
from django.views import generic
from movies.models import Movie
from movies.models import Character
from rest_framework import viewsets
from movies.serializers import MovieSerializer,CharacterSerializer
from django.db.models.functions import Concat
from django.db.models import CharField, Value
from movies.forms import CharacterForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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

class CharacterFormView(CreateView):
    template_name="movies/characterform.html"
    form_class=CharacterForm
    success_url=reverse_lazy("movies:movielist")

    def dispatch(self, request, *args, **kwargs):
        self.id_movie = kwargs["movie"]
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        form.instance.movie_id = self.id_movie
        self.object = form.save()
        return super().form_valid(form)
