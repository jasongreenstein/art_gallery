from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from .models import Art

# Create your views here.


class ArtListView(ListView):
    model = Art
    template_name = "gallery.html"


class SeriesListView(ListView):
    model = Art
    # queryset = Art.objects.order_by("series").distinct("series")
    queryset = set(Art.objects.values_list("series", flat=True))
    template_name = "series.html"


class ArtInSeriesListView(ListView):
    model = Art
    template_name = "art_in_series.html"

    def get_queryset(self):
        series = self.kwargs["series"]
        return Art.objects.filter(series=series)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["series"] = self.kwargs["series"]
        return context
