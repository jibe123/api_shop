from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from cart.serializers import CartSerializer
from cart.models import Cart


class CartViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
