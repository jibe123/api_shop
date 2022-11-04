from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer
from .models import Category, Product


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True, methods=['GET'], url_path='products')
    def get_products(self, request, *args, **kwargs):
        instance = self.get_object()
        products = instance.products.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
