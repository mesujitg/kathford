from django.shortcuts import render, HttpResponse
from products.models import Product


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def show_product_details(request, id):
    products = Product.objects.filter(id=id)
    product = Product.objects.get(id=id)
    # return HttpResponse(products[0].price)
    return HttpResponse(product.price)
