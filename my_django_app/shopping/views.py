from django.shortcuts import render, redirect
from django.contrib import messages
# from shopping.models import Wishlist, Cart, Order, Comment, Review
from shopping.models import *



def add_to_wishlist(request, pid):
    wl = Wishlist.objects.filter(user=request.user).filter(product_id=pid)
    if not wl:
        # wl = Wishlist(user_id=request.user.id, product_id=pid)
        wl = Wishlist(user=request.user, product=Product.objects.get(id=pid))
        wl.save()
        messages.info(request, 'Item added to you Wish list!')
    else:
        messages.info(request, 'Item already exists in your Wish list!')
    return redirect('home')


def remove_from_wishlist(request):
    pass


def add_to_cart(request, pid, qty):
    cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
    if not cart:
        cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
        cart.save()
        messages.info(request, 'Item added to you Cart!')
    else:
        messages.info(request, 'Item already exists in your Cart!')
    return redirect('home')


def remove_from_cart(request):
    pass


def checkout(request):
    pass


def comment(request):
    pass


def review(request):
    pass