# 💰 Personal Finance Tracker

Modern ve kullanıcı dostu kişisel finans yönetim uygulaması. Django ile geliştirilmiş, responsive tasarım ve interaktif grafiklerle finansal durumunuzu kolayca takip edin.

## ✨ Özellikler

### 📊 Dashboard
- **Anlık özet kartları** - Toplam gelir, gider ve bakiye
- **İnteraktif grafikler** - Chart.js ile kategori dağılımı ve aylık trendler
- **Son işlemler** listesi
- **Hızlı işlem** butonları

### 💳 İşlem Yönetimi
- **Gelir/Gider ekleme** - Kolay form ile işlem kaydetme
- **Kategori bazlı** organizasyon
- **Düzenleme ve silme** işlemleri
- **Tarih bazlı** filtreleme

### 🏷️ Kategori Sistemi
- **Özelleştirilebilir kategoriler**
- **Gelir/Gider** ayrımı
- **Renkli etiketler**
- **Admin panel** entegrasyonu

### 🔐 Kullanıcı Sistemi
- **Güvenli giriş/çıkış**
- **Kişisel veri güvenliği**
- **Kullanıcı bazlı** işlem yönetimi

## 🛠️ Teknoloji Stack

### Backend
- **Django 4.2** - Python web framework
- **SQLite** - Veritabanı (geliştirme)
- **Django Admin** - Yönetim paneli

### Frontend
- **Bootstrap 5** - CSS framework
- **Chart.js** - Grafik kütüphanesi
- **Font Awesome** - İkonlar
- **Vanilla JavaScript** - İnteraktivite

### Deployment
- **GitHub** - Versiyon kontrolü
- **Gunicorn** - WSGI server (production)
- **PostgreSQL** - Veritabanı (production)

## 🚀 Kurulum

### Gereksinimler
- Python 3.8+
- pip
- virtualenv (önerilen)

### Adım Adım Kurulum

1. **Repository'yi klonlayın:**
```bash
git clone https://github.com/fatihkayaci/personal-finance-tracker.git
cd personal-finance-tracker
```

2. **Virtual environment oluşturun:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Bağımlılıkları yükleyin:**
```bash
pip install -r requirements.txt
```

4. **Veritabanını ayarlayın:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Superuser oluşturun:**
```bash
python manage.py createsuperuser
```

6. **Geliştirme sunucusunu başlatın:**
```bash
python manage.py runserver
```

7. **Tarayıcıda açın:**
```
http://127.0.0.1:8000
```

## 📱 Kullanım

### İlk Kurulum
1. Admin panelinden giriş yapın (`/admin/`)
2. Kategoriler oluşturun (Yemek, Ulaşım, Maaş, vb.)
3. Ana sayfaya dönün ve ilk işleminizi ekleyin

### Günlük Kullanım
1. **Dashboard'a** göz atarak mali durumunuzu görün
2. **"Yeni İşlem Ekle"** ile gelir/giderlerinizi kaydedin
3. **Grafiklerle** harcama alışkanlıklarınızı analiz edin
4. **İşlemler sayfasından** geçmiş kayıtlarınızı yönetin

## 📁 Proje Yapısı

```
personal-finance-tracker/
├── finance_tracker/          # Ana proje ayarları
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/                # Ana sayfa app'i
│   ├── views.py             # Dashboard logic
│   ├── urls.py              # Dashboard routing
│   └── templates/           # Dashboard HTML
├── transactions/            # İşlem yönetimi app'i
│   ├── models.py           # Transaction & Category modelleri
│   ├── views.py            # İşlem CRUD operasyonları
│   ├── urls.py             # İşlem routing
│   ├── admin.py            # Admin panel ayarları
│   └── templates/          # İşlem HTML'leri
├── accounts/               # Kullanıcı yönetimi (gelecekte)
├── static/                 # CSS, JS, resimler
├── media/                  # Kullanıcı yüklemeleri
├── requirements.txt        # Python bağımlılıkları
└── manage.py              # Django yönetim scripti
```

## 🔧 Geliştirme

### Yeni Özellik Ekleme
1. Uygun app'e yeni view ekleyin
2. URL routing yapın
3. Template oluşturun
4. Test edin

### Veritabanı Değişiklikleri
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static Dosya Değişiklikleri
```bash
python manage.py collectstatic
```

## 🤝 Katkıda Bulunma

1. Bu repository'yi fork edin
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request oluşturun

## 📋 Yapılacaklar (Roadmap)

### v1.0 (Mevcut)
- [x] Temel dashboard
- [x] İşlem CRUD operasyonları
- [x] Kategori sistemi
- [x] Grafik entegrasyonu

### v1.1 (Planlanan)
- [ ] Kullanıcı kayıt/giriş sistemi
- [ ] Profile sayfası
- [ ] Bütçe hedefleri
- [ ] E-posta bildirimleri

### v1.2 (Gelecek)
- [ ] CSV import/export
- [ ] Raporlar (PDF)
- [ ] Mobil uygulama (React Native)
- [ ] API (Django REST Framework)

## 📜 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**Fatih KAYACI** - [GitHub](https://github.com/fatihkayaci) | [LinkedIn](https://www.linkedin.com/in/fatih-kayaci-79180a28a/)

## 🙏 Teşekkürler

- [Django](https://djangoproject.com/) - Web framework
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Chart.js](https://www.chartjs.org/) - Grafik kütüphanesi
- [Font Awesome](https://fontawesome.com/) - İkonlar

---
⭐ Bu projeyi beğendiyseniz yıldız vermeyi unutmayın!