from rest_framework.routers import DefaultRouter
from products.viewsets import *


router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('subcategories', SubCategoryViewSet)
router.register('types', TypeViewSet)
router.register('brands', BrandViewSet)
router.register('products', ProductViewSet)
