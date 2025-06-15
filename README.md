# 💰 Personal Finance Tracker

A modern and user-friendly personal finance management application. Built with Django, featuring responsive design and interactive charts to easily track your financial status.

## ✨ Features

### 📊 Dashboard
- **Real-time summary cards** - Total income, expenses, and balance
- **Interactive charts** - Category distribution and monthly trends with Chart.js
- **Recent transactions** list
- **Quick action** buttons

### 💳 Transaction Management
- **Add income/expenses** - Easy form for recording transactions
- **Category-based** organization
- **Edit and delete** operations
- **Date-based** filtering

### 🏷️ Category System
- **Customizable categories**
- **Income/Expense** separation
- **Colored labels**
- **Admin panel** integration

### 🔐 User System
- **Secure login/logout**
- **Personal data security**
- **User-based** transaction management

## 🛠️ Technology Stack

### Backend
- **Django 4.2** - Python web framework
- **SQLite** - Database (development)
- **Django Admin** - Management panel

### Frontend
- **Bootstrap 5** - CSS framework
- **Chart.js** - Charting library
- **Font Awesome** - Icons
- **Vanilla JavaScript** - Interactivity

### Deployment
- **GitHub** - Version control
- **Gunicorn** - WSGI server (production)
- **PostgreSQL** - Database (production)

## 🚀 Installation

### Requirements
- Python 3.8+
- pip
- virtualenv (recommended)

### Step-by-Step Installation

1. **Clone the repository:**
```bash
git clone https://github.com/fatihkayaci/personal-finance-tracker.git
cd personal-finance-tracker
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up database:**
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser:**
```bash
python manage.py createsuperuser
```

6. **Start development server:**
```bash
python manage.py runserver
```

7. **Open in browser:**
```
http://127.0.0.1:8000
```

## 📱 Usage

### Initial Setup
1. Login to admin panel (`/admin/`)
2. Create categories (Food, Transportation, Salary, etc.)
3. Return to homepage and add your first transaction

### Daily Usage
1. Check your **Dashboard** to view financial status
2. Use **"Add New Transaction"** to record income/expenses
3. **Analyze** spending habits with charts
4. **Manage** past records from transactions page

## 📁 Project Structure

```
personal-finance-tracker/
├── finance_tracker/          # Main project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── dashboard/                # Homepage app
│   ├── views.py             # Dashboard logic
│   ├── urls.py              # Dashboard routing
│   └── templates/           # Dashboard HTML
├── transactions/            # Transaction management app
│   ├── models.py           # Transaction & Category models
│   ├── views.py            # Transaction CRUD operations
│   ├── urls.py             # Transaction routing
│   ├── admin.py            # Admin panel settings
│   └── templates/          # Transaction HTML files
├── accounts/               # User management (future)
├── static/                 # CSS, JS, images
├── media/                  # User uploads
├── requirements.txt        # Python dependencies
└── manage.py              # Django management script
```

## 🔧 Development

### Adding New Features
1. Add new view to appropriate app
2. Configure URL routing
3. Create template
4. Test functionality

### Database Changes
```bash
python manage.py makemigrations
python manage.py migrate
```

### Static File Changes
```bash
python manage.py collectstatic
```


## 🤝 Contributing

1. Fork this repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Create Pull Request

## 📋 Roadmap

### v1.0 (Current)
- [x] Basic dashboard
- [x] Transaction CRUD operations
- [x] Category system
- [x] Chart integration

### v1.1 (Planned)
- [ ] User registration/login system
- [ ] Profile page
- [ ] Budget goals
- [ ] Email notifications

### v1.2 (Future)
- [ ] CSV import/export
- [ ] Reports (PDF)
- [ ] Mobile app (React Native)
- [ ] API (Django REST Framework)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 👨‍💻 Developer

**[Your Name]** - [GitHub](https://github.com/fatihkayaci) | [LinkedIn](https://www.linkedin.com/in/fatih-kayaci-79180a28a/)

## 🙏 Acknowledgments

- [Django](https://djangoproject.com/) - Web framework
- [Bootstrap](https://getbootstrap.com/) - CSS framework
- [Chart.js](https://www.chartjs.org/) - Charting library
- [Font Awesome](https://fontawesome.com/) - Icons

---
⭐ If you like this project, don't forget to give it a star!