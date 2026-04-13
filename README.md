# 🚀 Emplay Inc Backend (Prompt Nexus API)

## 📌 Project Overview

This is a backend API built using **Django** that allows users to create, view, and manage prompts. The application supports RESTful APIs and is deployed on **Render** with a **PostgreSQL database**.

---

## ⚙️ Tech Stack

* Python (Django)
* PostgreSQL (Render DB)
* Gunicorn (Production server)
* dj-database-url
* django-cors-headers

---

## 🌐 Live API

Base URL:

```
https://emplay-inc-backend.onrender.com/
```

---

## 📡 API Endpoints

### 1️⃣ Get All Prompts

```
GET /prompts/
```

Response:

```json
[
  {
    "id": "uuid",
    "title": "Prompt Title",
    "content": "Prompt Content",
    "complexity": 5
  }
]
```

---

### 2️⃣ Create Prompt

```
POST /prompts/
```

Body:

```json
{
  "title": "Sample Prompt",
  "content": "This is a sample prompt content",
  "complexity": 5
}
```

Response:

```json
{
  "message": "Prompt created",
  "id": "uuid"
}
```

---

### 3️⃣ Get Single Prompt

```
GET /prompts/<uuid>/
```

Response:

```json
{
  "id": "uuid",
  "title": "Prompt Title",
  "content": "Prompt Content",
  "complexity": 5,
  "view_count": 1
}
```

---

## 🧪 Testing

You can test APIs using:

* Thunder Client (VS Code)
* Postman

---

## ⚡ Local Setup

### 1. Clone repo

```
git clone https://github.com/vishwalavanya/Emplay-Inc-Backend.git
cd backend
```

### 2. Create virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Run migrations

```
python manage.py migrate
```

### 5. Run server

```
python manage.py runserver
```

---

## 🌍 Deployment (Render)

* Backend deployed using Render Web Service
* PostgreSQL database connected via `DATABASE_URL`
* Gunicorn used as WSGI server

---

## 🔐 Environment Variables

```
DATABASE_URL=your_postgres_url
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=*
```

---

## 🎯 Features

* Create and fetch prompts
* UUID-based unique IDs
* Input validation
* View count tracking (Redis ready)
* Production deployment

---

## 👨‍💻 Author

Vishwa Jaganathan

---

## 🚀 Future Improvements

* Authentication (JWT)
* Frontend (Angular)
* Redis full integration
* Pagination & filtering
