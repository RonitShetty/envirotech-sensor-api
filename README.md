# 🏭 EnviroTech Sensor API

A fully functional REST API built with **FastAPI** to manage and analyze data from industrial factory sensors. This project demonstrates core backend development principles including CRUD operations, data validation, routing, and custom middleware using in-memory mock data.

## 🚀 Features

* **Strict Data Validation:** Utilizes Pydantic to ensure all incoming sensor data strictly adheres to required types and formats.
* **Full CRUD Functionality:** Create, Read, Update, and Delete sensor records dynamically.
* **Smart Filtering:** Query parameters allow users to quickly isolate sensors based on their operational status.
* **Analytics Engine:** A custom endpoint that calculates aggregate factory health, including the count of broken machines and the average temperature of working ones.
* **Custom Middleware:** Implements a Python decorator (`@logging`) to intercept requests, process analytics, and log execution states automatically.

## ⚠️ Note on Data Persistence
Currently, this API utilizes an **in-memory Python list** pre-populated with dummy data for demonstration purposes. Any new sensors added via `POST` requests, or changes made via `PUT`/`DELETE`, will be lost if the Uvicorn server is restarted. Future iterations will include a dedicated SQLite database for true data persistence.

## 🛠️ Tech Stack
* **Language:** Python 3
* **Framework:** FastAPI
* **Validation:** Pydantic
* **Server:** Uvicorn

## 📡 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Welcome message and API health check |
| `GET` | `/sensors` | Returns all current sensor data |
| `POST` | `/add_sensor` | Adds a new sensor to the database |
| `GET` | `/sensor/filter?status={int}` | Returns sensors matching a specific status code |
| `PUT` | `/sensor/update/{target_id}` | Updates the temperature and status of an existing sensor |
| `DELETE` | `/sensor/delete_sensor/{target_id}`| Permanently removes a sensor from the system |
| `GET` | `/sensor/global_stats` | Returns aggregate analytics (avg temp, broken count) |

## 💻 Local Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
