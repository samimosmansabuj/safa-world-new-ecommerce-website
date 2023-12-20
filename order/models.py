from django.db import models
from account.models import Customer, Address
from product.models import Product
import random

# Create your models here.
class Wishlist(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product)
    
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.customer.first_name+' '+self.product.count()


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.customer.first_name} - {self.product.title} * {self.quantity}'


class OrderItem(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.PositiveIntegerField(default=1)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.customer.first_name} - {self.product.title} * {self.quantity} = {self.total_price}'


class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Unpaid', 'Unpaid'),
        ('Recieved', 'Recieved'),
        ('Processing', 'Processing'),
        ('On The Way', 'On The Way'),
        ('Delivered', 'Delivered'),
    )
    PAYMENT_METHOD = (
        ('COD', 'COD'),
        ('Bkash', 'Bkash'),
        ('Nagad', 'Nagad'),
        ('Bank', 'Bank'),
    )
    order_id = models.IntegerField(default=f'SafaWorld {random.randint(111111, 999999)}', db_index=True, unique=True, editable=False)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    orderitem = models.ManyToManyField(OrderItem)
    adress = models.ForeignKey(Address, on_delete=models.DO_NOTHING)
    
    shipping_charge = models.DecimalField(decimal_places=2, max_digits=10)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    
    is_paid = models.BooleanField(default=False)
    transaction_id = models.CharField(blank=True, null=True, max_length=150)
    status = models.CharField(choices=STATUS, default='Pending', max_length=150)
    payment_method = models.CharField(choices=PAYMENT_METHOD, default='COD', max_length=150)
    
    order_note = models.TextField(blank=True, null=True)
    order_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order_date']
    
    def __str__(self) -> str:
        return f'{self.customer.first_name} {self.customer.last_name} - {self.order_id}'
    


