from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product

User = get_user_model()


class Cart(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    order_items = models.ManyToManyField(Product)
