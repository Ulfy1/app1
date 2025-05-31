from django.shortcuts import render

from goods.models import Categories, Products

# Create your views here.
def catalog(request, category_slug):

    categories = Categories.objects.all()

    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug = category_slug)

    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'goods/product.html', context = context)
