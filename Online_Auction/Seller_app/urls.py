from django.urls import path
from . import views

urlpatterns = [
    path('productinfo/', views.ProductView.as_view(), name = 'product_url'),
    path('showproduct/', views.ShowproductView.as_view(), name = 'showproduct_url')
]