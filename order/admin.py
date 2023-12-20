from django.contrib import admin
from .models import Wishlist, Cart, OrderItem, Order

# Register your models here.
# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'product', 'id', 'created_date']

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     list_display = ['customer', 'product', 'quantity', 'product_price', 'total_price', 'updated_date', 'id']

admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(OrderItem)
admin.site.register(Order)


