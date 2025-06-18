from reviews.views import ReviewListView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from reviews import views

app_name = "reviews"

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'review', views.ReviewViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include(router.urls)),
    path("", ReviewListView.as_view(), name="reviewlist"),
]