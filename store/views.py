from django.shortcuts import render
from .models import Category

def homepage(request):
    all_categories = Category.objects.all()
    context = {
        "all_categories": all_categories
    }
    return render(request, "store/index.html", context)
