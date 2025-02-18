from django.db import models

class GalleryItem(models.Model):
    class Category(models.TextChoices):
        ILLUSTRATIONS = "Illustrations", "Illustrations"
        GRAFFITI = "Graffiti", "Graffiti"
        TATTOO = "Tattoo", "Tattoo"

    title = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.ILLUSTRATIONS)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="gallery_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title