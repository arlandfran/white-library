from django.shortcuts import render


def profile(request):
    """Return the user profile template"""

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
