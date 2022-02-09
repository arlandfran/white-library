from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product

# Create your views here.
def view_bag(request):
  """Returns shopping bag"""

  return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
  """Add product to bag"""

  redirect_url = request.POST.get('redirect_url')
  bag = request.session.get('bag', {})

  if item_id not in list(bag.keys()):
    bag[item_id] = 1
  
  request.session['bag'] = bag
  
  return redirect(redirect_url)

def remove_from_bag(request, item_id):
  """Remove product from bag"""

  try:
    product= get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})
    bag.pop(item_id)
    messages.success(request, f'Removed {product.name} from your bag')
    request.session['bag'] = bag
    return HttpResponse(status=200)
  except Exception as e:
    messages.error(request, f'Error removing item: {e}')
    return HttpResponse(status=500)