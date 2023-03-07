from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/categories', null=True, blank=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '1. Category'


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '2. Sub Category'


class Type(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.subcategory.category}-{self.subcategory}-{self.title}'

    class Meta:
        verbose_name = '3. Type'


class Brand(models.Model):
    title = models.CharField(max_length=255)
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '4. Brand'


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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '5. Product'

