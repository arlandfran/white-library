from email import message
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from products.models import Product

from .forms import ContactForm


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


def contact(request):
    """Return contact form"""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send()
            messages.success(
                request, 'Thank you for your feedback! You will receive an email shortly.')
            return redirect(reverse('contact'))
        else:
            messages.error(
                request, 'Contact form is invalid, please try again.')
            return redirect(reverse('contact'))
    else:
        form = ContactForm

    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
