from django.contrib import admin
from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        "category_name",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = [
        "subcategory_name",
        "category",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = [
        "brand_name",
        "user",
        "timestamp",
        "status"
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "product_name",
        "user",
        "timestamp",
        "status"
    ]
