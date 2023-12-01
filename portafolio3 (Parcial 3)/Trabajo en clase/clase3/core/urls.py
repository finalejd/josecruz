from django.urls import path

from core import views

app_name = "core"

urlpatterns = [
    path('create/product/', views.CreateProduct.as_view(), name="create_product"),
    path('list/product/', views.ListProduct.as_view(), name="list_product"),
    path('detail/product/<int:pk>/', views.DetailProduct.as_view(), name="detail_product"),
    path('update/product/<int:pk>/', views.UpdateProduct.as_view(), name="update_product"),
    path('delete/product/<int:pk>/', views.DeleteProduct.as_view(), name="delete_product"),
]