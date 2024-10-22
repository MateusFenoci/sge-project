# inflows/models.py

from django.db import models
from itens.models import Item
from suppliers.models import Supplier


class Inflow(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, related_name='inflows')
    item = models.ForeignKey(Item, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField(default=0)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.item.product} - {self.item.size}"
