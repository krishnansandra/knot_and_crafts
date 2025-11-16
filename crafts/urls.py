from django.urls import path
from . import views 

app_name = 'crafts'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('products/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/', views.ProductListView.as_view(), name='products'),
    path('product/add/', views.ProductCreateView.as_view(), name='product_add'),
    path('product/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('product/<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('admin/dashboard/', views.admin_products, name='admin_products'),
    
]



