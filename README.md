
# Student Management System

A web-based Student Management System built using Python and Django.

This application helps manage student records through a simple dashboard with authentication, CRUD operations, search functionality, and form validation.

## Features

- User Login and Logout
- Dashboard with student statistics
- Add new student records
- View student records
- Edit student details
- Delete student records
- Search students by name or register number
- Form validation
- Authentication-protected pages
- Django Admin integration

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS
- Git and GitHub

## Project Structure

```text
studentmanagementsystem/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── students/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│   └── registration/
│       └── login.html
│
├── .gitignore
├── manage.py
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/romannaveen16062005-oss/student-management-system.git
```

### 2. Open the project folder

```bash
cd student-management-system
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install Django python-dotenv
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost
```

Use a newly generated private secret key. Never upload `.env` to GitHub.

### 7. Apply migrations

```bash
python manage.py migrate
```

### 8. Create an admin account

```bash
python manage.py createsuperuser
```

### 9. Run the development server

```bash
python manage.py runserver 8080
```

Open in your browser:

http://127.0.0.1:8080/

## Run Tests

```bash
python manage.py test students
```

## Project Status

Core student management features, authentication, validation, and automated tests have been implemented.

## Author

Naveen

GitHub: https://github.com/romannaveen16062005-oss
