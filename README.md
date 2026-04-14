# 🚀 Emplay Inc Backend — Prompt Nexus API

## 📌 Project Overview

**Prompt Nexus API** is a production-ready backend system built using **Django** that allows users to create, manage, and retrieve prompts efficiently.

The system is designed with scalability, clean architecture, and real-world backend practices in mind. It includes support for tagging, validation, and deployment on cloud infrastructure.

---

## 🎯 Key Objectives

* Build a RESTful backend using Django
* Implement structured prompt storage
* Enable tagging system for categorization (Bonus B)
* Deploy using cloud infrastructure (Render — Bonus C)
* Prepare backend for frontend integration and authentication

---

## ⚙️ Tech Stack

| Technology          | Purpose                |
| ------------------- | ---------------------- |
| Python (Django 4.2) | Backend Framework      |
| PostgreSQL (Render) | Database               |
| Gunicorn            | Production WSGI Server |
| dj-database-url     | DB config handling     |
| django-cors-headers | Frontend integration   |
| UUID                | Secure ID generation   |

---

## 🌐 Live API

Base URL:

```
https://emplay-inc-backend.onrender.com/
```

---

## 📂 Core Features

### ✅ Prompt Management

* Create prompts
* Retrieve all prompts
* Retrieve single prompt

### ✅ Tagging System (Bonus B)

* Add multiple tags per prompt
* Stored using JSONField
* Helps in categorization & filtering

### ✅ Secure ID System

* UUID-based IDs (non-guessable)

### ✅ Input Validation

* Title length validation
* Content validation
* Complexity range (1–10)

### ✅ View Count Tracking

* Tracks number of times a prompt is accessed

### ✅ Deployment Ready (Bonus C)

* Hosted on Render
* PostgreSQL database integrated

---

## 📡 API Endpoints

---

### 🔹 1. Get All Prompts

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
    "complexity": 5,
    "tags": ["AI", "ML"],
    "created_at": "timestamp"
  }
]
```

---

### 🔹 2. Create Prompt

```
POST /prompts/
```

Request Body:

```json
{
  "title": "Sample Prompt",
  "content": "This is a sample prompt content",
  "complexity": 5,
  "tags": ["AI", "Backend"]
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

### 🔹 3. Get Single Prompt

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
  "tags": ["AI", "Backend"],
  "view_count": 1
}
```

---

## 🧪 API Testing

You can test APIs using:

* Thunder Client (VS Code)
* Postman
* Browser (GET requests)

---

## ⚡ Local Development Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/vishwalavanya/Emplay-Inc-Backend.git
cd backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create `.env` file:

```
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=prompt_nexus
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432
```

---

### 5️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 6️⃣ Start Development Server

```bash
python manage.py runserver
```

Server runs at:

```
http://127.0.0.1:8000/
```

---

## 🌍 Production Deployment (Render)

### 🔹 Build Command

```bash
pip install -r requirements.txt && python manage.py makemigrations && python manage.py migrate
```

---

### 🔹 Start Command

```bash
gunicorn prompt_nexus.wsgi:application
```

---

### 🔹 Environment Variables (Render)

```
DATABASE_URL=your_postgres_url
SECRET_KEY=your_secret_key
DEBUG=False
ALLOWED_HOSTS=*
```

---

## 🧠 Architecture Overview

* **Django Apps** → modular structure (`prompts`)
* **Models** → Prompt schema with tags
* **Views** → API handlers (GET, POST)
* **URLs** → Route mapping
* **Database** → PostgreSQL (cloud hosted)

---

## 🔒 Design Decisions

* Used **UUID** instead of auto-increment IDs for security
* Used **JSONField for tags** for flexibility
* Kept APIs simple for easy frontend integration
* Stateless API design

---

## 📊 Project Status

| Feature             | Status      |
| ------------------- | ----------- |
| Backend APIs        | ✅ Completed |
| Tagging System      | ✅ Completed |
| Deployment (Render) | ✅ Completed |
| Authentication      | ⏳ Pending   |
| Frontend (Angular)  | ⏳ Pending   |
| DevOps Enhancements | ⏳ Pending   |

---

## 🚀 Future Enhancements

* 🔐 Authentication (JWT / Firebase)
* 🔍 Tag-based filtering
* 📄 Pagination
* ⚡ Redis for caching & view count
* 🎨 Angular frontend integration

---

## 👨‍💻 Author

**Vishwa Jaganathan**

---

## 🏁 Conclusion

This project demonstrates real-world backend development including API design, database integration, deployment, and feature implementation like tagging.

It is structured to scale further with authentication, frontend integration, and advanced DevOps practices.
