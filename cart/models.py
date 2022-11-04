from django.contrib.auth import get_user_model
from django.db import models

from shop.models import Product

User = get_user_model()


class Cart(models.Model):
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    order_items = models.ManyToManyField(Product)

    @property
    def get_total(self):
        ordered_items = self.order_items.all()
        total = sum(item.price for item in ordered_items)
        return total

    def save(self, *args, **kwargs):
        self.total = self.get_total()
        super().save(*args, **kwargs)

