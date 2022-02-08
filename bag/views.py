from django.shortcuts import render

# Create your views here.
def view_bag(request):
  """Returns shopping bag"""

  return render(request, 'bag/bag.html')