from django.shortcuts import render, redirect
from django.conf import settings
from django.http import JsonResponse
import stripe
from .forms import OrderForm
from bag.contexts import bag_contents
from .models import Order, OrderItem
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout_view(request):
    bag = bag_contents(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if request.user.is_authenticated:
                order.user = request.user
            order.total_price = bag["total"]
            order.save()

            for item in bag["items"]:
                product = Product.objects.get(id=item["product_id"])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                    price=product.price,
                )

            # Create Stripe Payment Intent
            intent = stripe.PaymentIntent.create(
                amount=int(order.total_price * 100),  # Convert to cents
                currency="usd",
                metadata={"order_id": order.id}
            )
            order.stripe_payment_intent = intent.id
            order.save()

            return JsonResponse({"client_secret": intent.client_secret})
    
    else:
        form = OrderForm()

    return render(request, "checkout/checkout.html", {"form": form, "bag": bag})
