from django import forms
from .models import Product

#Formularios para productos


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "user",
            "subcategory",
            "product_name",
            "description",
            "brand",
            "stock",
            "price_cost",
            "image",
            "status",
            "slug"
        ] 
        widgets = {
            "user": forms.Select(attrs={"class":"form-select form-control"}),
            "subcategory": forms.Select(attrs={"class":"form-select form-control"}),
            "product_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre del Producto"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe la descripcion del Producto"}),
            "brand": forms.Select(attrs={"class":"form-select form-control"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "price_cost": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "image": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el codigo de busqueda del Producto"})
        }



class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "user",
            "subcategory",
            "product_name",
            "description",
            "brand",
            "stock",
            "price_cost",
            "image",
            "status",
            "slug"
        ] 
        widgets = {
            "user": forms.Select(attrs={"class":"form-select form-control"}),
            "subcategory": forms.Select(attrs={"class":"form-select form-control"}),
            "product_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre del Producto"}),
            "description": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe la descripcion del Producto"}),
            "brand": forms.Select(attrs={"class":"form-select form-control"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "price_cost": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "image": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "slug": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el codigo de busqueda del Producto"})
        }

