from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products, name='products'),
    path('details/<id>', views.show_product_details, name='single_product')
]
