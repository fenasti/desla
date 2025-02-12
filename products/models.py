from django.db import models

class Product(models.Model):
    class Category(models.IntegerChoices):
        ILLUSTRATION = 1, "Illustration"
        GRAFFITI = 2, "Graffiti"
        TATTOO = 3, "Tattoo"
        CLOTHE = 4, "Clothing"
        OTHER = 5, "Other"

    name = models.CharField(max_length=254)
    category = models.PositiveSmallIntegerField(choices=Category.choices, default=Category.OTHER)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)  # Allows up to 999999.99
    image = models.ImageField(upload_to="product_images/", blank=True, null=True)

    def __str__(self):
        return self.name