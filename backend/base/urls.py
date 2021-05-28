from django.urls import path
from .views import *


urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('', getRoutes, name='routes'),

    path('users/register/', registerUser, name='register'),
    path('users/profile/', getUserProfile, name='user-profile'),
    path('users/', getUsers, name='users'),


    path('products', getProducts, name='products'),
    path('products/<str:pk>', getSingleProduct, name='product'),
]