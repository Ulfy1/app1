from django.shortcuts import render

from goods.models import Categories, Products

# Create your views here.
def catalog(request):

    categories = Categories.objects.all()
    products = Products.objects.all()

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    return render(request, 'goods/product.html')