from django.shortcuts import render,redirect
from django.contrib import messages
from account.models import Customer, User
from product.models import Category, Product
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def registration(request):
    
    return render(request,'seller/registration.html')
 
def login_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        if not User.objects.filter(username=username).exists():
            messages.warning(request,'User not found. Please, Create an Account..')
            return redirect('login')
        else:
            user = authenticate(username=username, password=password)
            if not user:
                messages.warning(request,'Password does not match')
                return redirect('login')
            else:
                login(request,user)
                return redirect('dashboard')
    return render(request,'seller/login.html')

def logout_page(requset):
    logout(requset)
    return redirect('login')    
    

def dashboard(request):
    
    return render(request,'seller/dashboard.html')

def add_product(request):
   
    return render(request,'seller/add_product.html')

def product_list(request):
   
    return render(request,'seller/product_list.html')

def order_list(request):
   
    return render(request,'seller/order_list.html')