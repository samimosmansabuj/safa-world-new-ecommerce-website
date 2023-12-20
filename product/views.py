from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage

# Create your views here.
def product(request):
    product = Product.objects.all()
    item_per_page = 4
    
    paginator = Paginator(product, item_per_page)
    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except EmptyPage:
        product = paginator.page(1)
    except PageNotAnInteger:
        product = paginator.page(1)
    except InvalidPage:
        product = paginator.page(1)
    
    context = {'product': product, 'paginator': paginator, 'item_per_page': item_per_page}
    
    return render(request, 'product/product.html', context)

def single_product(request, id):
    product = Product.objects.get(id=id)
    
    context = {'product': product}
    return render(request, 'product/single_product.html', context)

