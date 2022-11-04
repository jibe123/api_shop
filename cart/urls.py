from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, OrderViewSet


router = DefaultRouter()

router.register('order', OrderViewSet)
router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
