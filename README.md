# University LMS & ERP System

A comprehensive Learning Management System (LMS) and Enterprise Resource Planning (ERP) solution for universities. This monorepo contains a Django REST Framework backend and a Next.js (TypeScript) frontend.

## 📁 Project Structure

- `backend/` — Django REST Framework project (API, Database Models)
- `frontend/` — Next.js + TypeScript Application (Dashboard, Student/Teacher Portals)
- `docs/` — Documentation

---

## 🛠 Prerequisites

Before starting, ensure you have the following installed:

- **Python 3.10+**
- **Node.js 18+** & **npm**
- **PostgreSQL** (Database)
- **Git**

---

## 🚀 Backend Setup (Django + PostgreSQL)

### 1. Database Setup (How to Generate DB)

Since we switched to PostgreSQL, you need to manually create the database before running the application.

1.  **Install PostgreSQL** if you haven't already.
2.  **Open your SQL tool** (pgAdmin, DBeaver, or command line `psql`).
3.  **Create the database** by running this SQL command:
    ```sql
    CREATE DATABASE university_lms_db;
    ```
4.  **Verify Credentials**:
    - Open `backend/.env` file.
    - Ensure `DATABASE_NAME`, `DATABASE_USER`, `DATABASE_PASSWORD` match your local PostgreSQL setup.
    - Default configuration provided:
      ```env
      DATABASE_ENGINE=django.db.backends.postgresql
      DATABASE_NAME=university_lms_db
      DATABASE_USER=postgres
      DATABASE_PASSWORD=postgres  <-- CHANGE THIS to your actual password
      DATABASE_HOST=localhost
      DATABASE_PORT=5432
      ```

### 2. Install Dependencies

Navigate to the backend directory and set up your Python environment.

```bash
cd backend

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Run Migrations

Apply the database schema to your new PostgreSQL database.

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Create Admin User

Create a superuser to access the Django Admin panel.

```bash
python manage.py createsuperuser
```

### 5. Run the Server

Start the Django development server.

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/`.

---

## 💻 Frontend Setup (Next.js)

### 1. Install Dependencies

Open a new terminal and navigate to the frontend directory.

```bash
cd frontend
npm install
```

### 2. Configure Environment

Ensure you have a `.env.local` file (or copy example).

```bash
cp .env.local.example .env.local
```

### 3. Run Development Server

Start the Next.js frontend.

```bash
npm run dev
```

The application will be accessible at `http://localhost:3000/`.

---

## ❓ Troubleshooting

**"psql is not recognized..."**
- If you can't run `psql` from the terminal, use the **SQL Shell (psql)** application installed with PostgreSQL or a GUI like **pgAdmin**.

**"password authentication failed for user..."**
- Double-check the `DATABASE_PASSWORD` in your `backend/.env` file. It must match the password you set during PostgreSQL installation.

**"database 'university_lms_db' does not exist"**
- The database is not created automatically. You MUST run the `CREATE DATABASE university_lms_db;` SQL command manually.
