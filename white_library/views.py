from django.shortcuts import render


def page_not_found(request, exception):
    template = '404.html'
    return render(request, template, status=400)
