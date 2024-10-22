from django.contrib import admin
from .models import Inflow

class InflowAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'item', 'quantity', 'created_at')
    search_fields = ('supplier__name', 'item__product__title', 'item__size')
    list_filter = ('supplier', 'item')

admin.site.register(Inflow, InflowAdmin)
