from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Modelo de productos (categorias)
class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=32, default="Generic Category Name")
    description = models.CharField(max_length=256, default="Generic Category Description")
    timestamp = models.DateField(auto_now_add=True)
    update_category = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.category_name
    
#Modelo de productos (suncategorias)
class SubCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=32, default="Generic SubCategory Name")
    description = models.CharField(max_length=256, default="Generic SubCategory Description")
    timestamp = models.DateField(auto_now_add=True)
    update_category = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.subcategory_name


#Modelo de marcas de productos
class Brand(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_name = models.CharField(max_length=32, default="Generic Brand Name")
    description = models.CharField(max_length=256, default="Generic Brand Description")
    timestamp = models.DateField(auto_now_add=True)
    update_category = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.brand_name
    
#Modelo de la informacion de los productos
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32, default="Generic Product Name")
    description = models.CharField(max_length=256, default="Generic Product Description")
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    price_cost = models.FloatField(default=0.0)
    image = models.ImageField(upload_to='products_images', blank=True, null=True) # configurar un servidor de media
    timestamp = models.DateField(auto_now_add=True)
    update_category = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField(default=True)
    slug = models.SlugField(max_length=16)

    def __str__(self):
        return self.product_name
    
