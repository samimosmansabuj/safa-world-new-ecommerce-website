from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_verified', 'is_seller', 'is_customer']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'phone_number', 'gender', 'date_of_birth', 'profile_picture']

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address_type', 'customer', 'upazila', 'district', 'country', 'post_code']



