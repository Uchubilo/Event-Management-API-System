
# 🎉 Event Management API System

A **FastAPI-powered backend system** designed to streamline the management of events, attendees, speakers, and registration workflows. This project provides a clean and modular foundation for building scalable event platforms.

---

## ✨ Key Features

* 🔐 **User Registration & Authentication**
  Each user is uniquely identified with a system-generated ID.

* 🗓️ **Event Management**
  Create, update, view, and delete events easily.

* 🧑‍🤝‍🧑 **User and Speaker Management**
  Manage attendee and speaker profiles.

* 📋 **Attendance Tracking**
  Log and track attendance for each event.

* 🔄 **Full CRUD Operations**
  Supports full Create, Read, Update, and Delete for:

  * Users
  * Events
  * Registrations

* 🧱 **Modular Codebase**
  Clearly separated components: models, schemas, services, and routes.

---

## ⚙️ Tech Stack

* **Python 3.9+**
* **FastAPI** – Web framework for building APIs
* **Pydantic** – Data validation and parsing
* **Uvicorn** – Lightning-fast ASGI server

---

## 📁 Project Directory Structure

```bash
.
├── app
│   ├── __init__.py
│   ├── main.py                # FastAPI app entry point
│   ├── database.py            # DB connection setup
│   ├── models.py              # Database models
│   ├── routes/                # API route handlers
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── events.py
│   │   └── registration.py
│   ├── schemas/               # Request and response models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   └── registration.py
│   ├── services/              # Business logic layer
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   └── registration.py
├── .gitignore
└── README.md
```

---

## 🚀 Getting Started

### Step 1: Clone the Repository


git clone 
cd Event-Management-API-System


### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies


pip install "fastapi[all]"


### Step 4: Run the Development Server


uvicorn app.main:app --reload


Access the API docs at:
📎 [http://localhost:8000/docs]

---

## 📖 API Documentation

FastAPI comes with interactive documentation:

* ✅ **Swagger UI**: `http://localhost:8000/docs`
* ✅ **ReDoc**: `http://localhost:8000/redoc`

---

## 🔌 Sample API Endpoints

| Method | Endpoint     | Description                  |
| ------ | ------------ | ---------------------------- |
| POST   | `/users/`    | Register a new user          |
| POST   | `/events/`   | Create a new event           |
| GET    | `/events/`   | List all events              |
| POST   | `/register/` | Register a user for an event |

---

## 📎 Additional Notes

* Ensure the FastAPI server is up and running before making requests.
* Database settings and connection details should be configured inside `database.py`.

---





