from lista import views
from django.urls import path

urlpatterns = [
#rejestracja użytkownika
    path('register', views.registerApi),
    path('user', views.userIdApi),
    path('login', views.loginApi),
    path('shop/<int:id>/', views.shopApi),
    path('shop', views.shopApi),
    path('products/<int:id>/', views.productApiShop),
    path('products', views.productApiShop),
    path('product/<int:id>/', views.productApi),
    path('product', views.productApi),

]