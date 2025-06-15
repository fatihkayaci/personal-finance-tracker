# transactions/urls.py
from django.urls import path
from . import views

app_name = 'transactions'

urlpatterns = [
    path('', views.transaction_list, name='list'),
    path('add/', views.add_transaction, name='add'),
    path('edit/<int:transaction_id>/', views.edit_transaction, name='edit'),
    path('delete/<int:transaction_id>/', views.delete_transaction, name='delete'),
]