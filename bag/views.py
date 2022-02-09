from django.shortcuts import render, redirect

# Create your views here.
def view_bag(request):
  """Returns shopping bag"""

  return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
  """Add product to bag"""

  redirect_url = request.POST.get('redirect_url')
  bag = request.session.get('bag', {})

  if item_id not in list(bag.keys()):
    bag[item_id] = 1
  
  request.session['bag'] = bag
  
  return redirect(redirect_url)