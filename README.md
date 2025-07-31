# 🚀 Employee Feedback Management API (Django + JWT)

A RESTful API-based Employee Feedback System where employees can submit feedback, and admins can view/analyze it using filters.
This project is built with Django REST Framework and JWT Authentication.

## ✅ Features
### 🔐 JWT Authentication
- User Registration & Login
- Access & Refresh tokens
### 👥 Employee & Designation Management
### 📝 Feedback Management
- Submit answers to multiple feedback questions at once
- View feedback by employee
- View feedback by designation
### 📊 Admin Panel
- Admins can filter feedback by designation, department, and date range

## 🏗️ Tech Stack
- Backend: Django, Django REST Framework
- Authentication: JWT (using djangorestframework-simplejwt)
- Database: SQLite

## Project Structure
```
employee_feedback/
├── employee_feedback/        # Project settings and configuration
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── feedback/                # Feedback app (models, views, serializers, urls)
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── fixtures/
│   │   └── initial_data.json
│   └── migrations/
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## Installation

### Prerequisites
- Python 3.8+
- pip
- (Optional) Virtual environment tool (venv)

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnsifMkr/employee_feedback.git
   cd employee_feedback
   ```
2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run migrations:**
   ```bash
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
5. **Load sample data:**
   ```bash
   python manage.py loaddata feedback/fixtures/initial_data.json
   ```
6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## Usage

Once the server is running, you can access the API endpoints using tools like Postman, curl, or via a frontend application.

The default server URL is: `http://127.0.0.1:8000`

## API Endpoints
| Method  | Endpoint | Description |
| POST	| /api/register/ | Register a new user |
| POST	| /api/login/ |	Login and get JWT tokens |
| POST	| /api/token/refresh/ |	Refresh JWT access token |
| GET	| /api/questions/?feedback_type=employee	| List feedback questions |
| POST	| /api/submit-feedback/	| Submit feedback |
| GET	| /api/employee/<employee_id>/feedback/	| View feedback by employee |
| GET	| /api/designation/<designation_name>/feedback/	| View feedback by designation |
| GET	| /api/admin/feedback/?designation=Developer&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD |	Admin: Filter feedback |


## Fixtures & Initial Data

To load sample data for testing:

```bash
python manage.py loaddata feedback/fixtures/initial_data.json
```



