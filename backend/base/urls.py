from django.urls import path
from .views import *

urlpatterns = [
    path('', getRoutes, name='routes'),
    path('products', getProducts, name='products'),
    path('products/<str:pk>', getSingleProduct, name='product'),
]