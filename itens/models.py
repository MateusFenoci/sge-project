from django.db import models
from products.models import Product
from size.models import Size

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='items')
    size = models.ForeignKey(Size, on_delete=models.PROTECT, related_name='items')
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    class Meta:
        unique_together = ['product', 'size']

    def __str__(self):
        return f"{self.product} - {self.size}"

