from django.contrib import admin
from .models import Outflow

class OutflowAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'created_at')
    search_fields = ('item__product__title', 'item__size', 'description')
    list_filter = ('item', 'created_at')

admin.site.register(Outflow, OutflowAdmin)
