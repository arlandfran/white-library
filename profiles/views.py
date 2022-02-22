from email.policy import default
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse

from .models import UserProfile
from .forms import UserForm, AddressForm

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


def details(request):
    """Return user profile details"""

    user = get_object_or_404(User, username=request.user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect(reverse('details'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = UserForm(instance=user)

    template = 'profiles/details.html'
    context = {
        'user': user,
        'form': form,
    }

    return render(request, template, context)


def address_book(request):
    """Return user's saved addresses"""

    user_profile = get_object_or_404(UserProfile, user=request.user)
    addresses = user_profile.addresses.all()
    default_address = user_profile.addresses.get(default=True)

    template = 'profiles/address_book.html'
    context = {
        'addresses': addresses,
        'default_address': default_address,
    }

    return render(request, template, context)
