from django.shortcuts import render, HttpResponse


def show_products(request):
    return render(request, 'products.html')


def show_product_details(request):
    return HttpResponse('Single Product')
