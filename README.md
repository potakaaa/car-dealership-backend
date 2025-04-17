# Car Dealership Backend

This is the backend for the **Car Dealership** web app. The backend is built using **FastAPI** and connects to a **PostgreSQL** database and a **Redis** instance. Docker is used to containerize the app for easy setup and deployment.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Setup](#setup)
  - [Setting Up the Backend with Docker](#setting-up-the-backend-with-docker)
  - [Local Setup (without Docker)](#local-setup-without-docker)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [License](#license)

---

## Technologies Used

- **FastAPI** – Web framework for building APIs.
- **PostgreSQL** – Relational database for storing car dealership data.
- **Redis** – In-memory data store (used as cache).
- **Docker** – Containerization for easy app setup and deployment.
- **Uvicorn** – ASGI server to serve the FastAPI app.
- **Python 3.11** – Programming language used to develop the app.

---

## Setup

### Setting Up the Backend with Docker

Follow these steps to set up the backend with Docker. This will automatically handle all dependencies, including **PostgreSQL** and **Redis**.

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/car-dealership-backend.git
   cd car-dealership-backend
   ```

2. **Create an `.env` file** for environment variables

   In the root directory of the project, create a `.env` file and add the following:

   ```env
   POSTGRES_USER=your_postgres_user
   POSTGRES_PASSWORD=your_postgres_password
   POSTGRES_DB=car_dealer
   REDIS_HOST=localhost
   REDIS_PORT=6379
   ```

3. **Build and start the Docker containers**

   Run the following command to build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

   This command will:
   - Build the FastAPI app container.
   - Pull the `PostgreSQL` and `Redis` images from Docker Hub.
   - Set up a **PostgreSQL** database and a **Redis** instance.
   - Expose **PostgreSQL** on port `5433` and **FastAPI** on port `8000`.

4. **Access the app**

   Once the Docker containers are running, you can access the backend via:

   - FastAPI: [http://localhost:8000](http://localhost:8000)
   - PostgreSQL: `localhost:5433` (using the credentials you set in the `.env` file)
   - Redis: `localhost:6379`

### Local Setup (without Docker)

If you prefer to run the app without Docker, follow these steps to set it up locally.

1. **Install dependencies**

   First, create a virtual environment and install the required dependencies.

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```

2. **Set up PostgreSQL**

   Make sure you have **PostgreSQL** running on your machine. You can use the following command to start the PostgreSQL service:

   ```bash
   sudo service postgresql start  # On Linux/macOS
   ```

   Create a new database, user, and set the password for your PostgreSQL instance.

   ```bash
   psql -U postgres
   CREATE DATABASE car_dealer;
   CREATE USER your_postgres_user WITH PASSWORD 'your_postgres_password';
   ALTER ROLE your_postgres_user SET client_encoding TO 'utf8';
   ALTER ROLE your_postgres_user SET default_transaction_isolation TO 'read committed';
   ALTER ROLE your_postgres_user SET timezone TO 'UTC';
   GRANT ALL PRIVILEGES ON DATABASE car_dealer TO your_postgres_user;
   ```

3. **Set up Redis**

   Make sure you have **Redis** running on your machine.

   ```bash
   redis-server
   ```

4. **Run the app**

   Start the FastAPI app using `uvicorn`:

   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

   This will run the FastAPI app on port 8000.

---

## Environment Variables

The app uses the following environment variables. Set these up in your `.env` file:

- `POSTGRES_USER` – PostgreSQL username
- `POSTGRES_PASSWORD` – PostgreSQL password
- `POSTGRES_DB` – Name of the PostgreSQL database
- `REDIS_HOST` – Redis server host (default: `localhost`)
- `REDIS_PORT` – Redis server port (default: `6379`)

---

## Usage

Once the app is running, you can:

- Access the FastAPI documentation at [http://localhost:8000/docs](http://localhost:8000/docs)
- Test endpoints with Postman or curl.

---

## License

This project is licensed under the MIT License.
