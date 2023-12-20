from django.urls import path
from .views import *

urlpatterns = [
    path('wishlist/', wishlist, name='wishlist'),
    path('cart/', cart_page, name='cart'),
    path('checkout/', checkout, name='checkout'),
    
]