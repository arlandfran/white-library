from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/', views.order_history, name='order_history'),
    path('order_history/<order_number>',
         views.order_summary, name='order_summary'),
    path('details/', views.details, name="details"),
]
