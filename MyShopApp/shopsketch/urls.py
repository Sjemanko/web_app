from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product/add', views.add_product),
    path('product/update/<int:id>', views.update_product),
    path('product/remove/<int:id>', views.delete_product),
    path('products/male', views.show_male_products),
    path('products/female', views.show_female_products),
]