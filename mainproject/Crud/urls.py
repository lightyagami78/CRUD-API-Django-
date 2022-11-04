from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    # Show list of datas

    path('product-view/<str:pk>/', views.productView, name="productView"),
    # show single data

    path('add-product',views.productAdd,name='productAdd'),
    # For Adding data

    path('update-product/<str:pk>/', views.productUpdate, name='productUpdate'),
    # For update the data

    path('delete-product/<str:pk>/', views.productDelete, name="productdelete")
    # for deleting the data
]
   