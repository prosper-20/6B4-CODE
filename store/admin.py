from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "category"]
    list_filter = ["category"]
    list_editable = ['price']


admin.site.register(Category)

admin.site.register(Product, ProductAdmin)
