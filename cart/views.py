from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cart.serializers import CartSerializer, OrderSerializer
from cart.models import Cart, Order


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
