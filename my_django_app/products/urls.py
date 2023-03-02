from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products),
    path('details', views.show_product_details)
]
