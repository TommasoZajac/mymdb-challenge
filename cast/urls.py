from django.urls import path,include
from rest_framework.routers import DefaultRouter
from cast import views
from cast.views import PersonListView

app_name = "cast"

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'cast', views.PersonViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path("", PersonListView.as_view(), name="personlist"),
]