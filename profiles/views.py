from django.core.exceptions import ObjectDoesNotExist
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


def delete_addresses(user_profile: UserProfile, delete_ids: list):
    for address_id in delete_ids:
        try:
            user_profile.addresses.get(id=address_id).delete()
        except ObjectDoesNotExist:
            print(f'address {address_id} does not exist, delete failed')


def set_default_address(user_profile: UserProfile, address_id: int):
    try:
        address = user_profile.addresses.get(id=address_id)
        address.default = True
        address.save()
    except ObjectDoesNotExist:
        print(f'address {address_id} does not exist, set as default failed')


def address_book(request):
    """Return user's saved addresses"""

    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        if 'default' in request.POST:
            address_id = request.POST['default']
            set_default_address(user_profile, address_id)
            redirect(reverse('address_book'))
        if 'delete' in request.POST:
            delete_ids = request.POST.getlist('delete')
            delete_addresses(user_profile, delete_ids)
            messages.success(request, f'{len(delete_ids)} item(s) deleted')
            redirect(reverse('address_book'))

    addresses = user_profile.addresses.all()

    if len(addresses) == 0:
        default_address = None
        total = 0
    else:
        try:
            default_address = user_profile.addresses.get(default=True)
            addresses = user_profile.addresses.filter(default=False)
            # addresses not default + default address
            total = len(addresses) + 1
        except ObjectDoesNotExist:
            default_address = None
            addresses = user_profile.addresses.filter(default=False)
            total = len(addresses)

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


def edit_address(request, address_id):

    user_profile = get_object_or_404(UserProfile, user=request.user)
    address = user_profile.addresses.get(id=address_id)

    if request.method == "POST":
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Address updated successfully')
            return redirect(reverse('address_book'))
    else:
        form = AddressForm(instance=address)

    template = 'profiles/edit_address.html'
    context = {
        'form': form,
        'address_id': address_id,
    }

    return render(request, template, context)
