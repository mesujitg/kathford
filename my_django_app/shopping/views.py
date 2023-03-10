from django.shortcuts import render, redirect
from django.contrib import messages
# from shopping.models import Wishlist, Cart, Order, Comment, Review
from shopping.models import *
from datetime import datetime
from django.contrib.auth.decorators import login_required



@login_required
def add_to_wishlist(request, pid):
    wl = Wishlist.objects.filter(user=request.user).filter(product_id=pid)
    if not wl:
        # wl = Wishlist(user_id=request.user.id, product_id=pid)
        wl = Wishlist(user=request.user, product=Product.objects.get(id=pid))
        wl.save()
        messages.info(request, 'Item added to you Wish list!')
    else:
        messages.info(request, 'Item already exists in your Wish list!')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_wishlist(request):
    pass


@login_required
def add_to_cart(request, pid, qty):
    cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
    if not cart:
        cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
        cart.save()
        messages.info(request, 'Item added to you Cart!')
    else:
        messages.info(request, 'Item already exists in your Cart!')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def add_to_cart_form(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        qty = request.POST['qty']

        cart = Cart.objects.filter(user=request.user).filter(product_id=pid)
        if not cart:
            cart = Cart(user=request.user, product=Product.objects.get(id=pid), qty=qty)
            cart.save()
            messages.info(request, 'Item added to you Cart!')
        else:
            messages.info(request, 'Item already exists in your Cart!')
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart(request):
    pass


@login_required
def comment(request):
    if request.method == 'POST':
        pid = request.POST['pid']
        cmt = request.POST['comment']

        comment = Comment(user=request.user, product_id=pid, comment=cmt)
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))


@login_required
def review(request):
    pass


@login_required
def show_wishlist(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    return render(request, 'user/wishlist.html', {'wishlist': wishlist})


@login_required
def show_cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'user/cart.html', {'cart': cart})


@login_required
def checkout(request):
    cart = Cart.objects.filter(user=request.user)

    if request.method == 'POST':
        mob=request.POST['mobile'],
        ad=request.POST['address']
        for c in cart:
            order = Order(user=request.user, mobile=mob,
                          address=ad, product=c.product,
                          qty=c.qty, price=c.product.price, 
                          date=datetime.now(),
                          discount=c.product.discount)
            order.save()
        
        messages.success(request, 'Your order is placed!')
        return redirect('home')

    data = []
    total = 0
    for c in cart:
        dt = {}
        dt['name'] = c.product.name
        dt['price'] = c.product.price
        dt['qty'] = c.qty
        dt['amount'] = (c.qty * c.product.price) - (c.qty*c.product.discount)
        dt['discount'] = c.product.discount
        total += dt['amount']
        data.append(dt)

    return render(request, 'user/checkout.html', {'data': data, 'total': total})