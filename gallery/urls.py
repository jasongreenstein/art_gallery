from django.urls import path

from .views import ArtListView

urlpatterns = [
    path("", ArtListView.as_view(), name="gallery"),
]
