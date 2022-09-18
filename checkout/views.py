from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LjR1WEONRUR7ONio03gg9VqBWEN9vODr1LEkD2pn5Fq7bV9wTkxa4BMyNyTb6WHRUm5wFvW6Wfg9j1oIrjLl5Kd009aXrmeqL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)