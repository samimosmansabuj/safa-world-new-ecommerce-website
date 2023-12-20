from django.shortcuts import render
from product.models import Product, Category

# Create your views here.
def home(request):
    category = Category.objects.all()
    product = Product.objects.all()
    context = {'category': category, 'product': product}
    return render(request, 'home/home.html', context)

def about_us(request):
    return render(request, 'home/about_us.html')

def contact_us(request):
    return render(request, 'home/contact_us.html')


