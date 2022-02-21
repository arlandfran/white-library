from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """Return the user profile template"""

    template = 'profiles/profile.html'

    return render(request, template)

def order_history(request):
    """Return the user' order history"""

    user_profile = get_object_or_404(UserProfile, user=request.user)
    orders = user_profile.orders.all()

    template = 'profiles/order_history.html'
    context = {
        'orders': orders,
    }

    return render(request, template, context)

def order_summary(request, order_number):
    """Return order summary of given order number"""

    order = get_object_or_404(Order, order_number=order_number)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)