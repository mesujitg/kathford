from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_products, name='products'),
    path('search/<key>', views.searched_products, name="searched_products"),
    path('classified/<genre>/<value>', views.classified_products, name="classified_products"),
    path('details/<id>', views.show_product_details, name='single_product')
]
