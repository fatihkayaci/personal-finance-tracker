from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', include('transactions.urls')),
    path('', include('dashboard.urls')),
]
