from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product

User = get_user_model()


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'


class Cart(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    order_items = models.ManyToManyField(Order)

    def __str__(self):
        return f'Cart # {self.id}'
