from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()
    total = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = '__all__'

    @staticmethod
    def get_total(obj):
        return sum(item.price for item in obj.order_items.all())



