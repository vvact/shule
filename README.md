
# 📚 EdTech Kenya – Revolutionizing Learning for Kenyan Students 🇰🇪

An innovative EdTech platform tailored for Kenyan learners, supporting **KCPE**, **KCSE**, and **CBC** curricula. This project provides access to curated study materials, quizzes, past papers, schemes of work, and more.

## 🔗 Live Demo

🚀 _Coming soon..._

---

## 💡 Features

- ✅ User registration & authentication (email/Google)
- ✅ Modern, responsive UI (Bootstrap, custom CSS)
- ✅ Password strength indicator and validation
- ✅ Role-based access (Students, Teachers, Admins)
- ✅ Study content (Notes, Past Papers, Topical Questions, Schemes of Work)
- ✅ Search & filter by subject, topic, class
- ✅ Quiz engine (auto-marking & feedback)
- ✅ Secure backend API with Django
- ✅ Mobile-first design for rural accessibility

---

## 📦 Tech Stack

| Layer         | Technology                 |
|---------------|----------------------------|
| Backend       | Django 5.x, Python 3.10+    |
| Frontend      | HTML5, CSS3, JS, Bootstrap |
| Auth          | Django Auth / Django AllAuth |
| DB            | SQLite / PostgreSQL        |
| Dev Tools     | Git, VS Code, Postman      |
| Hosting       | [Optional: Heroku, Render, Railway, etc.] |

---

## 🔧 Setup Instructions

### 1. 📁 Clone the Repo

```bash
git clone https://github.com/vvact/shule.git
cd edtech-kenya
```

### 2. 🐍 Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. ⚙️ Environment Variables

Create a `.env` file and configure:

```env
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### 5. 🛠 Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. 👤 Create Superuser

```bash
python manage.py createsuperuser
```

### 7. 🚀 Run Development Server

```bash
python manage.py runserver
```

Visit: `http://127.0.0.1:8000/`

---

## 📁 Project Structure

```txt
edtech-kenya/
├── accounts/           # User registration and login
├── core/               # Static pages (home, about)
├── materials/          # Study content (notes, quizzes, papers)
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🌍 Kenyan Curriculum Coverage

- ✅ CBC (Competency Based Curriculum)
- ✅ 8-4-4 system (Class 1–8, Form 1–4)
- ✅ KNEC past papers (KCPE, KCSE)
- ✅ Schemes of Work by term
- ✅ MOE-aligned study notes and quizzes

---

## 🎯 Vision

To empower learners in **Kenya** — especially in rural and underserved regions — by offering **accessible, curriculum-aligned** educational content online.

---

## 🤝 Contributing

We welcome contributions!

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-name`
3. Commit: `git commit -m "Add feature"`
4. Push: `git push origin feature-name`
5. Create a Pull Request

---

## 📄 License

MIT License — free to use and modify.

---

## 🙌 Acknowledgements

- Teachers and curriculum experts contributing content
- Django and open-source communities
- Kenyan students inspiring this project

---

## 📬 Contact

- ✉️ Email: yourname@example.com
- 🌐 Website: [Coming Soon]
- 🐦 Twitter: [@yourhandle]
