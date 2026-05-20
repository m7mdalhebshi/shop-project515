from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.customer_home, name='customer_home'),
    path('', views.customer_list, name='customer_list'),
    path('<int:pk>/', views.customer_detail, name='customer_detail'),
    path('new/', views.customer_create, name='customer_create'),
    path('<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('api/', views.CustomerListCreateAPI.as_view(), name='customer_api'),
]
