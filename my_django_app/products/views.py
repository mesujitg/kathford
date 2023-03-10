from django.shortcuts import render, HttpResponse
from products.models import Product
from shopping.models import Comment


def show_products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})


def show_product_details(request, id):
    # products = Product.objects.filter(id=id)
    product = Product.objects.get(id=id)
    comments = Comment.objects.filter(product_id=id)
    return render(request, 'product_details.html', {'product': product, 'comments': comments})
