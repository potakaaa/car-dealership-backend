# 🚗 Car E-Commerce API

An API service built using **FastAPI** to power a car e-commerce platform. It supports listing, buying, and selling cars, all within a clean, modular architecture.

---

## 📦 Features

- ✅ List all available cars
- ➕ Add a new car for sale
- 🛒 Buy a car (mark as sold)
- 🔍 View individual car details
- ❌ Delete a car listing
- 🔐 (Optional) Authentication for sellers and buyers

---

## 🧱 Tech Stack

- **FastAPI** – lightning-fast modern Python framework
- **Pydantic** – data validation and serialization
- **SQLAlchemy** – ORM for DB interaction
- **SQLite** (can be swapped with PostgreSQL for production)

---

## 📁 Project Structure

```bash
car_ecommerce_api/
├── app/
│   ├── main.py               # FastAPI app instance
│   ├── models/               # DB models
│   │   └── car.py
│   ├── schemas/              # Pydantic request/response models
│   │   └── car.py
│   ├── routes/               # API endpoints
│   │   └── car.py
│   ├── services/             # Business logic
│   │   └── car_service.py
│   ├── db/                   # Database setup
│   │   └── database.py
│   └── config.py             # App settings
├── requirements.txt
└── README.md
