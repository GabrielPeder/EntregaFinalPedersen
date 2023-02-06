from django.contrib import admin
from Products.models import Product


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'stock', 'style')
    list_filter = ('stock', 'style')
    search_fields = ('name', )