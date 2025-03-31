from django.shortcuts import render
from .models import GalleryItem

def gallery_view(request):
    items = GalleryItem.objects.all()
    return render(request, "gallery/gallery.html", {"items": items})