# Event Management API System

This is a **FastAPI-based Event Management API System** that allows users to:

* Register for events
* Track attendance
* Manage events, users, and speaker details

## 🚀 Features

* User registration and authentication using a generated ID 
* CRUD operations for Events, Users, and Registrations
* Attendance tracking
* Modular code structure (schemas, routes, services, etc.)

---

## 🛠️ Tech Stack

* Python 3.9+
* FastAPI
* Pydantic
* Uvicorn

---

## 📦 Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── events.py
│   │   ├── registration.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── registration.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── event.py
│   │   ├── registration.py
│   ├── models.py
│   └── main.py
├── .gitignore
└── README.md
```

---

## 🔧 Installation & Running the App

### 1. Clone the repository

```bash
git clone https://github.com/OnyekachiEzeala/Event-Management-API-System.git
cd Event Management API System
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install "fastapi[all]".
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) to access the interactive Swagger UI.

---

## 📝 API Documentation

Once the server is running, navigate to:

* Swagger UI: `http://localhost:8000/docs`

---

## ✅ Example Endpoints

* `POST /users/` - Create a user
* `POST /events/` - Create an event
* `GET /events/` - List events
* `POST /register/` - Register a user for an event

---

## 📌 Note

* Make sure your server is running and accessible.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📫 Contact

For any questions or support:

* Email: [ezesam227@gmail.com](mailto:ezesam227@gmail.com)
* GitHub: OnyekachiEzeala
