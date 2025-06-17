from movies.views import MovieListView,CharacterListView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movies import views

app_name = "movies"

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'movie', views.MovieViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path("", MovieListView.as_view(), name="movielist"),
    path("characters", CharacterListView.as_view(), name="characterlist"),
]