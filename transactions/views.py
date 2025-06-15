# transactions/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Transaction, Category

@login_required
def transaction_list(request):
    """Tüm işlemleri listele"""
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    
    # Toplam hesaplamalar
    total_income = sum(t.amount for t in transactions if t.transaction_type == 'income')
    total_expense = sum(t.amount for t in transactions if t.transaction_type == 'expense')
    balance = total_income - total_expense
    
    context = {
        'transactions': transactions,
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'page_title': 'İşlemlerim'
    }
    return render(request, 'transactions/list.html', context)

@login_required
def add_transaction(request):
    """Yeni işlem ekle"""
    if request.method == 'POST':
        # Form verilerini al
        amount = request.POST.get('amount')
        description = request.POST.get('description')
        transaction_type = request.POST.get('transaction_type')
        category_id = request.POST.get('category')
        date = request.POST.get('date')
        
        # Yeni işlem oluştur
        transaction = Transaction.objects.create(
            user=request.user,
            amount=amount,
            description=description,
            transaction_type=transaction_type,
            category_id=category_id,
            date=date
        )
        
        messages.success(request, 'İşlem başarıyla eklendi!')
        return redirect('transactions:list')
    
    # GET request - formu göster
    categories = Category.objects.filter(user=request.user)
    context = {
        'categories': categories,
        'page_title': 'Yeni İşlem'
    }
    return render(request, 'transactions/add.html', context)

@login_required
def edit_transaction(request, transaction_id):
    """İşlem düzenle"""
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    
    if request.method == 'POST':
        # Güncelle
        transaction.amount = request.POST.get('amount')
        transaction.description = request.POST.get('description')
        transaction.transaction_type = request.POST.get('transaction_type')
        transaction.category_id = request.POST.get('category')
        transaction.date = request.POST.get('date')
        transaction.save()
        
        messages.success(request, 'İşlem güncellendi!')
        return redirect('transactions:list')
    
    # GET request - formu göster
    categories = Category.objects.filter(user=request.user)
    context = {
        'transaction': transaction,
        'categories': categories,
        'page_title': 'İşlem Düzenle'
    }
    return render(request, 'transactions/edit.html', context)

@login_required
def delete_transaction(request, transaction_id):
    """İşlem sil"""
    transaction = get_object_or_404(Transaction, id=transaction_id, user=request.user)
    transaction.delete()
    messages.success(request, 'İşlem silindi!')
    return redirect('transactions:list')