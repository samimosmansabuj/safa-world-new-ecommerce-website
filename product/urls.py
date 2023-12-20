from django.urls import path
from .views import *

urlpatterns = [
    path('product/', product, name='product'),
    path('single-product/<int:id>/', single_product, name='single_product'),
]