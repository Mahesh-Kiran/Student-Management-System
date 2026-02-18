# EduHub - Student Management System

A simple web app I built to manage student records. You can add students, view them, search through them, and delete them. Nothing too fancy — just a clean CRUD app built with Django and deployed on Railway.

**Live demo:** https://student-management-system-production-c799.up.railway.app/

---

## What it does

- Add new student records
- View all students in one place
- Search for a specific student
- Delete student records
- Shows a count of how many students are in the system

That's pretty much it. It's meant to be straightforward and easy to use.

---

## Tech used

- **Python / Django** — backend framework
- **HTML / CSS** — frontend (kept it simple)
- **Docker** — containerized so it runs the same everywhere
- **Railway** — where it's deployed and hosted

---

## Running it locally

Make sure you have Python installed before you start.

**1. Clone the repo**
```bash
git clone https://github.com/Mahesh-Kiran/Student-Management-System.git
cd Student-Management-System
```

**2. Set up a virtual environment** (optional but recommended)
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

Then open your browser and go to `http://127.0.0.1:8000/`

---

## Running with Docker

If you prefer Docker:

```bash
docker build -t student-management .
docker run -p 8000:8000 student-management
```

Then visit `http://localhost:8000/`

---

## Project structure

```
Student-Management-System/
│
├── My_Project/        # Django project settings
├── Student_App/       # The main app (models, views, urls, templates)
├── manage.py
├── requirements.txt
├── Dockerfile
├── Procfile           # for deployment
└── runtime.txt        # Python version
```

---

## Deployment

This project is deployed on **Railway** using Docker. The `Dockerfile` and `Procfile` are already set up so you can deploy it pretty easily if you want to fork and host your own version.

---

## Contributing

Feel free to fork this and make it your own. If you find a bug or have a suggestion, open an issue and I'll take a look.

---

## Author

Made by [Mahesh-Kiran](https://github.com/Mahesh-Kiran)