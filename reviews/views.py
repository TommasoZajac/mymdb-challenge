from django.shortcuts import render
from django.views import generic
from reviews.models import Review
from reviews.serializers import ReviewSerializer, ReviewCreateSerializer
from rest_framework import viewsets
from reviews.filters import ReviewFilter
class ReviewListView(generic.ListView):
    model=Review
    template_name="reviews/reviewslist.html"

class ReviewViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                      IsOwnerOrReadOnly]
    filterset_class = ReviewFilter

    def get_serializer_class(self):
        if(self.action=="create"):
            return ReviewCreateSerializer
        return super().get_serializer_class()
    
    
    #togli filtro a livello di viewset
    #def get_queryset(self):
    #    qs = super().get_queryset()
    #    qs = qs.filter(content_type__app_label="movies",content_type__model="movie")
    #    return qs
    

