from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    created_by = serializers.CurrentUserDefault()

    class Meta:
        model = Cart
        fields = '__all__'
