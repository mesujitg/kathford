from django.contrib import admin
from products.models import Category, SubCategory, Type, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'category')


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption', 'subcategory')


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title', 'caption')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'brand', 'price', 'stock', 'image', 'discount' , 'status')
    