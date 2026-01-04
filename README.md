### ⚠️ Usage & Copyright Notice

This project is a personal portfolio project created to demonstrate my
full-stack development skills.

You may view and evaluate the source code for learning and recruitment purposes only.

- ❌ Commercial use is not permitted
- ❌ Redistribution without permission is not permitted
- ❌ Claiming this project as your own work is not permitted

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

This project demonstrates **real-world software engineering practices**, including:
- API-first backend development
- Clean frontend architecture
- Dockerized infrastructure
- CI/CD automation using GitHub Actions

---

## ✨ Key Features

### 🔐 Authentication
- JWT-based login & registration
- Secure protected routes
- Token refresh handling

### 🧠 Skills Management
- Create, update, and delete skills
- Skill categories (Frontend, Backend, DevOps, etc.)
- Proficiency and experience tracking

### 📁 Projects & Milestones
- Project CRUD operations
- Project status tracking (planned, in-progress, completed)
- Milestone creation & completion toggle
- Skill-to-project linking

### 📊 Dashboard & Analytics
- Project progress overview
- Milestone completion statistics
- Skill usage insights

---

## 🧱 Tech Stack

### Frontend
- React + TypeScript
- Vite
- Tailwind CSS
- React Query

### Backend
- Django
- Django REST Framework
- JWT Authentication

### Database
- PostgreSQL

### DevOps
- Docker & Docker Compose
- GitHub Actions (CI)
- Environment-based configuration

---

## 📂 Project Structure
```
SKILLSYNC-V3/
├── .github/
│ └── workflows/
│ └── ci.yml
├── skillsync-backend/
├── skillsync-frontend/
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
```
docker compose up --build
```

### 3️⃣ Access the app

- Frontend: http://localhost:8080

- Backend API: http://localhost:8000

### 🤖 CI/CD

This project uses GitHub Actions for Continuous Integration.

On every push and pull request, the pipeline:

- Installs dependencies

- Builds frontend & backend

- Ensures project integrity

### CI workflow file:
```
.github/workflows/ci.yml
```

### 👤 Author & Contact

- MD FAIZAN
- Full-Stack Developer

- GitHub: https://github.com/faizangit123

- Email: faizanrock705@gmail.com

### ⭐ Support

- If you find this project useful:

### ⭐ Star the repository

- 🍴 Fork it

- 📚 Use it as a learning reference