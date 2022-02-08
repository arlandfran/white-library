def bag_contents(request):

  bag_items = []
  product_count = 0

  context = {
    'bag_items': bag_items,
    'product_count': product_count,
  }

  return context