from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('practice', views.practice,name='pracitce'),
    path('<str:email>/', views.checkinginfo),
    path('category', views.category,name='category'),
    path('<str:product_name>', views.product_detail, name='product_detail'),

]
