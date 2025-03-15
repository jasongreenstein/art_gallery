from django.urls import path

from .views import ArtListView, SeriesListView, ArtInSeriesListView

urlpatterns = [
    path("", ArtListView.as_view(), name="gallery"),
    path("series/", SeriesListView.as_view(), name="series"),
    path("series/<str:series>/", ArtInSeriesListView.as_view(), name="art_in_series"),
]
