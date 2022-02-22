from django.utils.datastructures import MultiValueDictKeyError
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse

from checkout.models import Order

from .models import UserProfile
from .forms import UserForm, AddressForm


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

    user = get_object_or_404(get_user_model(), username=request.user)

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

    if request.method == "POST":
        try:
            default_id = request.POST['default'][0]
            delete_ids = request.POST['delete']
            address = user_profile.addresses.get(id=default_id)
            address.default = True
            for address_id in delete_ids:
                user_profile.addresses.get(id=address_id).delete()
        except MultiValueDictKeyError:
            address = user_profile.addresses.get(id=default_id)
            address.default = True
        finally:
            address.save()
            messages.success(request, 'Addresses updated successfully')
        return redirect(reverse('address_book'))

    addresses = user_profile.addresses.all()

    if len(addresses) == 0:
        default_address = None
        total = 0
    else:
        default_address = user_profile.addresses.get(default=True)
        addresses = user_profile.addresses.filter(default=False)
        total = len(addresses) + 1  # addresses not default + default address

    template = 'profiles/address_book.html'
    context = {
        'addresses': addresses,
        'default_address': default_address,
        'total': total,
    }

    return render(request, template, context)


def add_address(request):
    """Return add address form and template"""

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.profile = user_profile
            instance.save()
            messages.success(request, 'Address added successfully')
            return redirect(reverse('address_book'))
        else:
            messages.error(request,
                           ('Update failed. Please ensure '
                            'the form is valid.'))
    else:
        form = AddressForm()

    template = 'profiles/add_address.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
