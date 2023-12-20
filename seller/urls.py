from django.urls import path
from .views import *

urlpatterns = [
    path('seller/',login_page,name='login'), 
    path('logout/',logout_page,name='logout'), 
    path('registration/',registration,name='registration'),
    path('dashboard/',dashboard,name='dashboard'),
    path('add_product/',add_product,name='add_product'),
    path('product_list/',product_list,name='product_list'),
    path('order_list/',order_list,name='order_list'),
]