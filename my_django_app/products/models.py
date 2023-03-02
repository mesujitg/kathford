from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


class Type(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


class Brand(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)


class Product(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products')
    discount = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    details = models.TextField(null=True, blank=True)
    features = models.TextField(null=True, blank=True)
    specification = models.TextField(null=True, blank=True)

