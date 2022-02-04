from django.shortcuts import render

# Create your views here.
def index(request):
  """Return Index page"""
  return render(request, 'home/index.html')