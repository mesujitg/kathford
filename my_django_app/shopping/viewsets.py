from django.http import request
from rest_framework import viewsets
from shopping.models import *
from shopping.serializers import *


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all(user=request.user)
    serializer_class = CartSerializer
    permission_classes = ['IsAuthenticated']


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all(user=request.user)
    serializer_class = OrderSerializer
