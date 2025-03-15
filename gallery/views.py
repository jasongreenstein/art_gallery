from django.shortcuts import render
from django.views.generic import ListView
from .models import Art

# Create your views here.


class ArtListView(ListView):
    model = Art
    template_name = "gallery.html"
    gallery = Art.objects.all()
