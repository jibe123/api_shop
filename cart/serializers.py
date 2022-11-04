from rest_framework import serializers

from cart.models import Cart, Order


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    @staticmethod
    def get_total(obj):
        return sum(item.item.price*item.quantity for item in obj.order_items.all())


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()

    class Meta:
        model = Order
        fields = '__all__'
