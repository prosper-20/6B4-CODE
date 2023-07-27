from django.shortcuts import render
from .models import Category, Product

def homepage(request):
    all_categories = Category.objects.all()
    all_products = Product.objects.all()
    men_product = Product.objects.filter(category=1)
    women_product = Product.objects.filter(category=2)
    context = {
        "all_categories": all_categories,
        "all_products": all_products,
        "men_product": men_product,
        "women_product": women_product
    }
    return render(request, "store/index.html", context)

def detailpage(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, "store/detail.html", context)
