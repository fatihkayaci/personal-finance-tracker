# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.utils import timezone
from datetime import datetime, timedelta
import json
import calendar
from transactions.models import Transaction, Category

@login_required
def index(request):
    """Dashboard ana sayfası"""
    
    # Kullanıcının tüm işlemleri
    user_transactions = Transaction.objects.filter(user=request.user)
    
    # Bugün ve bu ay
    today = timezone.now().date()
    current_month = today.replace(day=1)
    
    # === TOPLAM HESAPLAMALAR ===
    total_income = user_transactions.filter(
        transaction_type='income'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    total_expense = user_transactions.filter(
        transaction_type='expense'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    balance = total_income - total_expense
    
    total_transactions = user_transactions.count()
    
    # === BU AYIN HESAPLAMALARI ===
    monthly_transactions_qs = user_transactions.filter(
        date__year=current_month.year,
        date__month=current_month.month
    )
    
    monthly_income = monthly_transactions_qs.filter(
        transaction_type='income'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    monthly_expense = monthly_transactions_qs.filter(
        transaction_type='expense'
    ).aggregate(total=Sum('amount'))['total'] or 0
    
    monthly_balance = monthly_income - monthly_expense
    monthly_transactions = monthly_transactions_qs.count()
    
    # === SON İŞLEMLER ===
    recent_transactions = user_transactions.order_by('-date', '-created_at')[:8]
    
    # === KATEGORİ ANALİZİ (Bu ay - sadece giderler) ===
    category_expenses = monthly_transactions_qs.filter(
        transaction_type='expense'
    ).values('category__name').annotate(
        total=Sum('amount')
    ).order_by('-total')
    
    category_labels = [item['category__name'] for item in category_expenses]
    category_data = [float(item['total']) for item in category_expenses]
    
    # === AYLIK TREND (Son 6 ay) ===
    monthly_labels = []
    monthly_income_data = []
    monthly_expense_data = []
    
    for i in range(5, -1, -1):  # Son 6 ay
        month_date = current_month - timedelta(days=i*30)
        month_date = month_date.replace(day=1)
        
        # Ay ismi
        month_name = calendar.month_name[month_date.month]
        monthly_labels.append(f"{month_name[:3]} {month_date.year}")
        
        # O ayın işlemleri
        month_transactions = user_transactions.filter(
            date__year=month_date.year,
            date__month=month_date.month
        )
        
        # Gelir
        month_income = month_transactions.filter(
            transaction_type='income'
        ).aggregate(total=Sum('amount'))['total'] or 0
        monthly_income_data.append(float(month_income))
        
        # Gider
        month_expense = month_transactions.filter(
            transaction_type='expense'
        ).aggregate(total=Sum('amount'))['total'] or 0
        monthly_expense_data.append(float(month_expense))
    
    # JSON formatına çevir (JavaScript için)
    context = {
        # Kullanıcı bilgisi
        'today': today,
        
        # Özet kartları
        'total_income': total_income,
        'total_expense': total_expense,
        'balance': balance,
        'total_transactions': total_transactions,
        
        # Bu ayın özeti
        'monthly_income': monthly_income,
        'monthly_expense': monthly_expense,
        'monthly_balance': monthly_balance,
        'monthly_transactions': monthly_transactions,
        
        # Son işlemler
        'recent_transactions': recent_transactions,
        
        # Chart verisi (JSON formatında)
        'category_labels': json.dumps(category_labels),
        'category_data': json.dumps(category_data),
        'monthly_labels': json.dumps(monthly_labels),
        'monthly_income_data': json.dumps(monthly_income_data),
        'monthly_expense_data': json.dumps(monthly_expense_data),
    }
    
    return render(request, 'dashboard/index.html', context)

# Opsiyonel: API endpoint (AJAX için)
@login_required  
def dashboard_data(request):
    """Dashboard verilerini JSON olarak döner (AJAX için)"""
    # Yukarıdaki hesaplamaların aynısı ama sadece JSON return
    pass