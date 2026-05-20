# EduHub — Student Management System

A web app I built to manage student records. You can add students, view them, search through them, edit their details, and delete them. Started as a simple CRUD project and I kept improving it — added pagination, caching, and duplicate protection along the way.


---

## What it does

- Add new student records
- View all students in a paginated table — 5 per page
- Search by name, email, or course — the footer count updates with results too
- Edit or delete any student
- Duplicate email protection — same student can't be added twice
- ETag caching — pages load faster on repeat visits if nothing changed

---

## Tech used

- **Python / Django** — backend
- **Bootstrap 5** — frontend
- **SQLite** — database
- **Gunicorn + Whitenoise** — production server and static files
- **Docker** — containerized for deployment
- **Vercel** — where it's hosted

---

## Running it locally

**1. Clone the repo**
```bash
git clone https://github.com/Mahesh-Kiran/Student-Management-System.git
cd Student-Management-System
```

**2. Set up a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run migrations**
```bash
python manage.py migrate
```

**5. Start the server**
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`

---

## Running with Docker

**Option A — Just the CRUD app (original)**
```bash
docker pull maheshkiran/student-management-system:latest
docker run -p 8000:8000 -e PORT=8000 maheshkiran/student-management-system:latest
```

**Option B — With pagination, ETag caching and idempotency (v2.0)**
```bash
docker pull maheshkiran/student-management-system_v2.0:latest
docker run -p 8000:8000 -e PORT=8000 maheshkiran/student-management-system_v2.0:latest
```

**Option C — Build from source**
```bash
docker build -t student-management .
docker run -p 8000:8000 -e PORT=8000 student-management
```

Open `http://localhost:8000/` — press `Ctrl + C` to stop.

> Data resets when the container stops since SQLite lives inside it. Fine for testing.

---

## Contributing

Fork it and make it your own. Found a bug or have a suggestion — open an issue.

---

## Author

Made by [Mahesh-Kiran](https://github.com/Mahesh-Kiran)