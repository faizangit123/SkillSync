# SkillSync 🚀  
**Full-Stack Skill & Project Tracking Platform**

![CI](https://github.com/faizangit123/skillsync/actions/workflows/ci.yml/badge.svg)
![Django](https://img.shields.io/badge/Django-REST%20Framework-092E20?logo=django)
![React](https://img.shields.io/badge/React-TypeScript-61DAFB?logo=react)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-316192?logo=postgresql)

---

## 📌 Overview

**SkillSync** is a **production-ready full-stack web application** designed to help developers track their **skills, projects, milestones, and progress analytics**.

The project demonstrates **real-world software engineering practices**, including:

- API-first backend development
- Clean, scalable frontend architecture
- JWT-based authentication
- Dockerized infrastructure
- CI/CD automation using GitHub Actions
- Cloud deployment (Render + Vercel)

---

## ✨ Key Features

### 🔐 Authentication
- JWT-based login & registration
- Secure protected routes
- Access & refresh token handling
- Auto-login after registration

### 🧠 Skills Management
- Create, update, and delete skills
- Skill categorization (Frontend, Backend, DevOps, etc.)
- Proficiency level & experience tracking

### 📁 Projects & Milestones
- Project CRUD operations
- Project status tracking (Planned, In Progress, Completed)
- Milestone creation and completion toggle
- Skill-to-project relationship mapping

### 📊 Dashboard & Analytics
- Project progress overview
- Milestone completion statistics
- Skill usage insights
- User-based data isolation

---

## 🧱 Tech Stack

### Frontend
- React + TypeScript
- Vite
- Tailwind CSS
- Axios
- Context API
- Modular component architecture

### Backend
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- RESTful API design
- Environment-based settings

### Database
- PostgreSQL 16.11

### DevOps & Infrastructure
- Docker & Docker Compose
- GitHub Actions (CI)
- Render (Backend Hosting)
- Vercel (Frontend Hosting)

---

## 🏗️ Architecture Overview
```
Browser (Client)
|
v
Frontend (React + Vite) ---> Backend (Django REST)
| |
v v
Vercel Render
|
v
PostgreSQL
```
---


## 📂 Project Structure
```
SKILLSYNC-V3/
├── .github/
│ └── workflows/
│ └── ci.yml
├── skillsync-backend/
│ ├── apps/
│ ├── core/
│ ├── manage.py
│ └── Dockerfile
├── skillsync-frontend/
│ ├── src/
│ ├── public/
│ ├── vite.config.ts
│ └── Dockerfile
├── docker-compose.yml
├── .gitignore
├── LICENSE
└── README.md
```


---

## 🚀 Local Development

### 1️⃣ Clone the repository
```bash
git clone https://github.com/faizangit123/skillsync.git
cd skillsync
```

### 2️⃣ Run with Docker
```bash
- Copy code
```docker compose up --build
```
### 3️⃣ Access the application

- Frontend: http://localhost:8080

- Backend API: http://localhost:8000

### 🌍 Production Deployment
# Backend (Render)
- Dockerized Django application

- Gunicorn WSGI server

- PostgreSQL database

- Environment-based configuration

# Frontend (Vercel)
- Vite production build

- Environment variable–based API connection

- Optimized static hosting

---

### 🔐 Environment Variables
# Frontend (Vercel)
```
env
Copy code
VITE_API_BASE_URL=https://skillsync-w0lo.onrender.com
```
# Backend (Render)
```
env
Copy code
DEBUG=False
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://...
ALLOWED_HOSTS=skillsync-w0lo.onrender.com
```
### 🤖 CI/CD Pipeline
- This project uses GitHub Actions for Continuous Integration.

# On every push & pull request:
- Install dependencies

- uild frontend & backend

- Validate project integrity

---

### 📄 CI Workflow:

```bash
Copy code
.github/workflows/ci.yml
```
---

### 🔒 Security Considerations
- JWT authentication with refresh tokens

- Environment-based secrets

- CORS protection

- User-based data access control

- Production-ready backend configuration

---

### 📡 API Design
- RESTful endpoints

- Token-based authentication

- Clear separation of concerns

- API-first approach (frontend easily replaceable)

### 👤 Author & Contact
- MD FAIZAN
- Full-Stack Developer

---
#LINK - GitHub: https://github.com/faizangit123

##LINK - Email: faizanrock705@gmail.com
---

### ⭐ Support
- If you find this project useful:

# ⭐ Star the repository

- 🍴 Fork it

- 📚 Use it as a learning reference

