from django.db import models

class Product(models.Model):
    class Category(models.IntegerChoices):
        PRINTS = 1, "Prints"
        PAINTING = 2, "Paintings"
        CLOTHE = 3, "Clothing"
        OTHER = 4, "Other"
        

    name = models.CharField(max_length=254)
    category = models.PositiveSmallIntegerField(choices=Category.choices, default=Category.OTHER)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Allows up to 999999.99
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def __str__(self):
        return self.name