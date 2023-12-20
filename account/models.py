from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from .managers import BaseManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, validators=[UnicodeUsernameValidator], unique=True)
    email = models.EmailField(max_length=200, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = BaseManager()
    
    is_customer = models.BooleanField(default=False)
    is_seller = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    auth_token = models.CharField(max_length=500, blank=True,null=True)
    otp_token = models.CharField(max_length=6, blank=True, null=True)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    
    def __str__(self) -> str:
        return self.username


class Customer(User):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=14)
    gender = models.CharField(choices=GENDER, blank=True, null=True, max_length=20)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='customer/profile_pic/', blank=True, null=True)


class Address(models.Model):
    ADDRESS_TYPE = (
        ('Shipping Address', 'Shipping Address'),
        ('Billing Address', 'Billing Address'),
        ('Address', 'Address'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    address_type = models.CharField(choices=ADDRESS_TYPE, default='Address', max_length=50)
    address = models.CharField(max_length=600, blank=True, null=True)
    upazila = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    post_code = models.CharField(max_length=4, blank=True, null=True)
    country = models.CharField(max_length=30, blank=True, null=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['updated_date']
    
    def __str__(self) -> str:
        return self.customer+' '+self.address_type
    
    
    
    

