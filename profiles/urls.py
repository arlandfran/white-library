from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_history/<order_number>',
         views.order_summary, name='order_summary'),
    path('details/', views.details, name="details"),
    path('address_book/', views.address_book, name="address_book"),
    path('address_book/add', views.add_address, name="add_address"),
    path('address_book/edit/<address_id>',
         views.edit_address, name="edit_address"),
    path('saved', views.saved, name='saved'),
    path('saved/remove/<product_id>', views.remove, name='remove_product'),
    path('admin/', views.admin, name='admin'),
    path('admin/add/', views.add_product, name='add_product'),
    path('admin/edit/<int:product_id>/',
         views.edit_product, name='edit_product'),
    path('admin/delete/',
         views.delete_product,
         name='delete_product'),
]
