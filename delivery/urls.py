from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.DeliveryHomeView.as_view(), name='delivery_home'),
    path('list/', views.DeliveryListView.as_view(), name='delivery_list'),
    path('create/', views.DeliveryCreateView.as_view(), name='delivery_create'),
    path('<int:pk>/', views.DeliveryDetailView.as_view(), name='delivery_detail'),
    path('<int:pk>/update/', views.DeliveryUpdateView.as_view(), name='delivery_update'),
    path('<int:pk>/delete/', views.DeliveryDeleteView.as_view(), name='delivery_delete'),
    path('api/', views.DriverListCreateAPI.as_view(), name='driver_api'),
]
