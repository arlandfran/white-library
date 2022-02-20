from django.shortcuts import render, get_object_or_404

from .models import UserProfile
from .forms import UserProfileForm


def profile(request):
    """Return the user profile template"""

    user_profile = get_object_or_404(UserProfile, user=request.user)
    form = UserProfileForm(instance=user_profile)
    orders = user_profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)
