from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'item_name',
        'item_price',
        'meal_type',
        'author',
        'created_at'
    )
    list_filter = ('meal_type', 'created_at')
    search_fields = ('item_name', 'item_description')
    ordering = ('-created_at', 'item_price')
