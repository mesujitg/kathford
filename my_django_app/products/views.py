from django.shortcuts import render, HttpResponse


def show_products(request):
    return HttpResponse('All Products')


def show_product_details(request):
    return HttpResponse('Single Product')
