from django.urls import path, include
from . import views

urlpatterns = [
    path('products/', views.product_list),
    path('product/add', views.add_product),
    path('product/update/<int:id>', views.update_product),
    path('product/delete/<int:id>', views.delete_product),
    path('products/male', views.show_male_products),
    path('products/female', views.show_female_products),
    path('cart/create', views.create_shopping_cart),
    path('orders/', views.show_my_orders),
    path('order/create', views.create_order),
    path('order/delete/<int:id>', views.remove_order),
    path('order/update/<int:id>', views.update_order),
    path('order/<int:id>', views.show_order),
    path('carts/', views.get_carts),
    path('order/confirm_order/<int:id>', views.confirm_order)
    
]