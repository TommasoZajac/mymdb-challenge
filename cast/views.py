from django.shortcuts import render
from django.views import generic
from cast.models import Person
from rest_framework import viewsets
from cast.serializers import PersonSerializer
class PersonListView(generic.ListView):
    model=Person
    template_name="cast/personlist.html"

class PersonViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly]
    