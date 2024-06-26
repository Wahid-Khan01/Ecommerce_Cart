from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='ShopHome'),
    path('about/', views.about, name='AboutUs'),
    path('contact/', views.contact, name='ContactUs'),
    path('tracker/', views.tracker, name='Tracker'),
    path('search/', views.search, name='Search'),
    path('product/<int:myid>', views.productView, name='Product View'),
    path('checkout/', views.checkout, name='Checkout'),
    path('tracker/', views.tracker, name='Tracker'),
    path('calculator/', views.calculator, name='calculator'),
]