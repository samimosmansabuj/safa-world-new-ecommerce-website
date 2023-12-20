from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated_date', 'created_date', 'short_description']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'quantity', 'current_price', 'discount_price', 'is_active', 'updated_date', 'id']



