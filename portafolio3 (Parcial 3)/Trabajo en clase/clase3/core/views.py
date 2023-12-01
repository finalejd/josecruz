from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy
from .models import *
from .forms import *

# Create your views here CRUD

class CreateProduct(LoginRequiredMixin, generic.CreateView):
    template_name = "core/create_product.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("core:list_product")
    login_url = reverse_lazy("home:index")


class ListProduct(LoginRequiredMixin, generic.View):
    template_name = "core/list_product.html"
    context = {}
    login_url = reverse_lazy("home:index")

    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(status=True)
        self.context = {
            "products": products
        }
        return render(request, self.template_name, self.context)

class DetailProduct(LoginRequiredMixin, generic.View):
    template_name = "core/detail_product.html"
    context = {}
    login_url = reverse_lazy("home:index")

    def get(self, request, pk, *args, **kwargs):
        product = Product.objects.get(pk=pk)
        self.context = {
            "product": product
        }
        return render(request, self.template_name,self.context)

class UpdateProduct(LoginRequiredMixin, generic.UpdateView):
    template_name = "core/update_product.html"
    model = Product
    form_class = UpdateProductForm
    success_url = reverse_lazy("core:list_product")
    login_url = reverse_lazy("home:index")

class DeleteProduct(LoginRequiredMixin, generic.DeleteView):
    template_name = "core/delete_product.html"
    model = Product
    success_url = reverse_lazy("core:list_product")
    login_url = reverse_lazy("home:index")


