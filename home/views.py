from django.shortcuts import render
from products.models import Product

# Create your views here.
def index(request):
  """Return Home page, including latest products"""

  latest_products = Product.objects.order_by('-id')[:6]

  context = {
    'products': latest_products
  }

  return render(request, 'home/index.html', context)