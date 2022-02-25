from django.shortcuts import render
from products.models import Product


def index(request):
    """Return Home page, including latest products"""

    latest_products = Product.objects.order_by('-id')[:6]
    template = 'home/index.html'
    context = {
        'products': latest_products
    }

    return render(request, template, context)


def legal(request):
    """Return disclaimer page"""

    template = 'home/legal.html'

    return render(request, template)
