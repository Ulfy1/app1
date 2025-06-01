from django.shortcuts import render
from django.core.paginator import Paginator

from goods.models import Categories, Products

# Create your views here.
def catalog(request, category_slug):
    
    page = request.GET.get('page', 1)
    max_price = request.GET.get('max_price')
    min_price = request.GET.get('min_price')


    categories = Categories.objects.all()

    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = Products.objects.filter(category__slug = category_slug)

    

    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    paginator = Paginator(products, 4)
    current_page = paginator.page(page)

    products = products.order_by('id')

    context = {
        'categories': categories,
        'products': current_page,
        'slug_url': category_slug,
    }
    return render(request, 'goods/catalog.html', context)

def product(request, product_slug):

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, 'goods/product.html', context = context)
