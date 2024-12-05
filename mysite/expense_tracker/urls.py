from django.urls import path
from . import views

urlpatterns = [
    # Web Views
    path('', views.transaction_list, name='transaction_list'),
    path('transaction/new/', views.transaction_create, name='transaction_create'),
    path('transaction/<int:pk>/edit/', views.transaction_edit, name='transaction_edit'),
    path('transaction/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    
    # API Views
    path('api/transactions/', views.TransactionListCreateAPI.as_view(), name='transaction_list_api'),
    path('api/transactions/<int:pk>/', views.TransactionDetailAPI.as_view(), name='transaction_detail_api'),
    path('monthly-summary/', views.monthly_summary, name='monthly_summary'),

]
