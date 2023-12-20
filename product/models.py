from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    short_description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['updated_date']
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=600)
    product_image_01 = models.ImageField(upload_to='product/image/')
    product_image_02 = models.ImageField(upload_to='product/image/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, blank=True, null=True, decimal_places=2)
    short_description = models.TextField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    
    is_active = models.BooleanField(default=True)
    is_stock = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['updated_date']
    
    def __str__(self) -> str:
        return self.title

