from django.db import models
from products.models import Product
from accounts.models import User
# from django.contrib.auth.models import User


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField()
    address = models.TextField()
    mobile = models.CharField(max_length=20)
    price = models.FloatField()
    discount = models.FloatField()
    date = models.DateField()
    status = models.CharField(max_length=255, 
                              choices=[
                                ('Requested', 'Requested'),
                                ('Dispatched', 'Dispatched'),
                                ('Delivered', 'Delivered'),
                                ('Cancelled', 'Cancelled'),
                                       ], default='Requested')
    
'''
product1 - Rs. 120000 - 2022
-----------------------------
-----------------------------

product1 - Rs. 130000 - 2023
----------------------------
----------------------------
'''

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review = models.CharField(max_length=255, null=True, blank=True)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='reviews', null=True, blank=True)
