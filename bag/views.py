from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """Return shopping bag template"""

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """Add product to bag"""

    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        messages.error(request, f'{product.name} is already in your bag')
    else:
        messages.success(request, f'{product.name} has been added to your bag')
        bag[item_id] = 1

    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove product from bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(
            request, f'{product.name} has been removed from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)
    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500)


def clear_bag(request):
    """Remove all products from bag"""

    request.session['bag'] = {}
    messages.success(request, "Your bag has been cleared")
    return HttpResponse(status=200)
