from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.CharField(max_length=70)
    image = models.ImageField(upload_to="category_images")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)# Allows empty values
    image = models.ImageField(upload_to="product_images")
    rating = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



    


