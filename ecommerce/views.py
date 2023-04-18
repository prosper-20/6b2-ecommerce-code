from django.shortcuts import render
from .models import Product


def product_page(request):
    products = Product.objects.all()
    # equipments = Equipment.objects.all()

    context = {
        "all_products": products,
    }
    return render(request, "product.html", context)

def product_single_page(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, "single.html", context)


def about(request):
    return render(request, 'about.html')

