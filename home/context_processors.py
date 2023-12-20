from product.models import Category, Product

def all_categories(request):
    all_category = Category.objects.all()
    return {'all_category': all_category}

def all_products(request):
    all_product = Product.objects.all()
    return {'all_product': all_product}


