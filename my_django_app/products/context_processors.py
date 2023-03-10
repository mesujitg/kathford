from products.models import *


def get_category(request):
    categories = Category.objects.all()
    subcategories = SubCategory.objects.all()
    types = Type.objects.all()
    brands = Brand.objects.all()
    return {'categories': categories, 'subcategories': subcategories, 
            'types': types, 'brands': brands}

