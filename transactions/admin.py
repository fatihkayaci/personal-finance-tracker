# transactions/admin.py

from django.contrib import admin
from .models import Category, Transaction

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'user', 'created_at']
    list_filter = ['category_type', 'created_at']
    search_fields = ['name']

@admin.register(Transaction)  
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['description', 'amount', 'transaction_type', 'category', 'date', 'user']
    list_filter = ['transaction_type', 'date']
    search_fields = ['description']
    date_hierarchy = 'date'