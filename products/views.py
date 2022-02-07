from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def all_products(request):
  """Return all products, including sorting and filtering"""

  products = Product.objects.all()

  context = {
    'products': products,
  }

  return render(request, 'products/products.html', context)

def product_detail(request, product_id):
  """Return individual product details"""

  product = get_object_or_404(Product, pk=product_id)

  context = {
    'product': product,
  }

  return render(request, 'products/product_detail.html', context)