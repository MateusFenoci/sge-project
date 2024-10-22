from django.contrib import admin
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'size', 'created_at', 'updated_at']
    search_fields = ['product', 'size']
    list_filter = ['product', 'size']
    list_per_page = 10

admin.site.register(Item, ItemAdmin)