import uuid  # used to generate the order number

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django.utils import timezone
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    # order no is going to be automatically generated,
    # we want it to be unique & permanent so users can find previous orders
    order_number = models.CharField(
        max_length=24,
        null=False,
        editable=False,
        unique=True,
        default=uuid.uuid4().hex[:24].upper()
    )
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True,
        blank=True,  # Can be null, but if provided must not be blank
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,  # Full name must be provided
        default=''
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False,  # Email must be provided
        default=''
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,  # Phone number must be provided
        default=''
    )
    country = CountryField(
        blank_label='Country *',
        null=False,
        blank=False,  # Country must be provided
        default='DE'  # Default country, can be changed if necessary
    )
    postcode = models.CharField(
        max_length=20,
        null=False,
        blank=False,  # Postcode must be provided
        default=''
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False,  # Town or city must be provided
        default=''
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False,  # Street address 1 must be provided
        default=''
    )
    street_address2 = models.CharField(
        max_length=80,
        null=False,  # Street address 2 must be provided
        blank=False,
        default=''
    )
    county = models.CharField(
        max_length=80,
        null=False,  # County must be provided
        blank=False,
        default=''
    )

    # auto_now_add automatically sets the date and time
    # when the order is created
    date = models.DateTimeField(
        auto_now_add=True,
    )

    # these last 3 fields are calculated using a model method
    # each time an order is saved
    delivery_cost = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        default=0.00  # Default delivery cost
    )
    order_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0.00  # Default order total
    )
    grand_total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        default=0.00  # Default grand total
    )
    original_bag = models.TextField(
        null=False,
        blank=False,
        default=''  # Default empty original bag
    )
    stripe_pid = models.CharField(
        max_length=254,
        null=False,
        blank=False,
        default=''  # Default empty stripe payment ID
    )

    def _generate_order_number(self):
        """
        Generates a random, unique 32 character string we can use
        as an order number using UUID.
        Method prepended with _ by convention to indicate
        a private method which will only be used in this class
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs
        """
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):

    order = models.ForeignKey(
        Order,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name='lineitems'
    )
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    product_size = models.CharField(
        max_length=5,
        null=True,
        blank=True
    )  # Sizes: XS, S, M, L, XL
    quantity = models.IntegerField(
        null=False,
        blank=False,
        default=0
    )
    lineitem_total = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False,
        editable=False
    )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.name} on order {self.order.order_number}'