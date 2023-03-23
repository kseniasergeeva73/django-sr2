from django.urls import path

from . import views

urlpatterns = [
    path('customers/', views.customer),
    path('sellers', views.seller),
    path('form/', views.sellers),
    path('form2/',views.customers),
]
