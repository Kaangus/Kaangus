from django.urls import path, base

from .views import *

urlpatterns = [
    path('', base, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductPageView.as_view(), name='product_page')
]
