from django.shortcuts import render

# Create your views here.
def wishlist(request):
    return render(request, 'order/wishlist.html')

def cart_page(request):
    return render(request, 'order/cart.html')

def checkout(request):
    return render(request, 'order/checkout.html')

def checkout(request):
    return render(request, 'order/checkout.html')





