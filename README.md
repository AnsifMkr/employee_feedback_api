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
| Method | Endpoint                                                                               | Description                  |
| ------ | -------------------------------------------------------------------------------------- | ---------------------------- |
| `POST` | `/api/register/`                                                                       | Register a new user          |
| `POST` | `/api/login/`                                                                          | Login and get JWT tokens     |
| `POST` | `/api/token/refresh/`                                                                  | Refresh JWT access token     |
| `GET`  | `/api/questions/?feedback_type=employee`                                               | List feedback questions      |
| `POST` | `/api/submit-feedback/`                                                                | Submit feedback              |
| `GET`  | `/api/employee/<employee_id>/feedback/`                                                | View feedback by employee    |
| `GET`  | `/api/designation/<designation_name>/feedback/`                                        | View feedback by designation |
| `GET`  | `/api/admin/feedback/?designation=Developer&start_date=YYYY-MM-DD&end_date=YYYY-MM-DD` | Admin: Filter feedback       |

### ✅ 1. Register a new user

```POST /api/register/```
- Request
```
{
  "username": "emma",
  "email": "emma@example.com",
  "password": "password123"
}
```
- Response
```
{
  "id": 11,
  "username": "emma",
  "email": "emma@example.com"
}
```
### ✅ 2. Login and get JWT tokens

```POST /api/login/```
- Request
```
{
  "username": "alice",
  "password": "admin123"
}
```
- Response
```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9..."
}
```
### ✅ 3. Refresh JWT Access Token

```POST /api/token/refresh/```
- Request
```
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```
- Response
```
{
  "access": "new_access_token_here"
}
```
### ✅ 4. List Feedback Questions

```GET /api/questions/?feedback_type=employee```
Authorization: Bearer <access_token>
- Response
```
[
  { "id": 1, "question_text": "How do you rate your work environment?", "feedback_type": "employee" },
  { "id": 2, "question_text": "How do you rate team collaboration?", "feedback_type": "employee" },
  { "id": 3, "question_text": "Do you have clarity on company policies?", "feedback_type": "employee" }
]
```
### ✅ 5. Submit Feedback

```POST /api/submit-feedback/```
Authorization: Bearer <access_token>
- Request
```
{
  "employee": 1,
  "designation": "Developer",
  "answers": [
    { "question": 1, "rating": 5, "comment": "Excellent environment!" },
    { "question": 2, "rating": 4, "comment": "Good teamwork and collaboration" }
  ]
}
```
- Response
```
{
  "id": 21,
  "employee_name": "john_doe",
  "designation": "Developer",
  "submitted_by": "alice",
  "created_at": "2025-07-31T11:45:00Z",
  "answers": [
    { "question": 1, "question_text": "How do you rate your work environment?", "rating": 5, "comment": "Excellent environment!" },
    { "question": 2, "question_text": "How do you rate team collaboration?", "rating": 4, "comment": "Good teamwork and collaboration" }
  ]
}
```
### ✅ 6. View Feedback by Employee

```GET /api/employee/1/feedback/```
Authorization: Bearer <access_token>
- Response
```
[
  {
    "id": 21,
    "employee_name": "john_doe",
    "designation": "Developer",
    "submitted_by": "alice",
    "created_at": "2025-07-31T11:45:00Z",
    "answers": [
      { "question": 1, "question_text": "How do you rate your work environment?", "rating": 5, "comment": "Excellent environment!" },
      { "question": 2, "question_text": "How do you rate team collaboration?", "rating": 4, "comment": "Good teamwork and collaboration" }
    ]
  }
]
```
### ✅ 7. View Feedback by Designation

```GET /api/designation/Developer/feedback/ ```
Authorization: Bearer <access_token>
- Response

```
[
  {
    "id": 21,
    "employee_name": "john_doe",
    "designation": "Developer",
    "submitted_by": "alice",
    "created_at": "2025-07-31T11:45:00Z",
    "answers": [
      { "question": 1, "question_text": "How do you rate your work environment?", "rating": 5, "comment": "Excellent environment!" }
    ]
  }
]
```
### ✅ 8. Admin Feedback View (Filter by designation, department, date range)

```GET /api/admin/feedback/?designation=Developer&start_date=2025-07-01&end_date=2025-07-31```
Authorization: Bearer <admin_access_token>
- Response
```
[
  {
    "id": 21,
    "employee_name": "john_doe",
    "designation": "Developer",
    "submitted_by": "alice",
    "created_at": "2025-07-31T11:45:00Z",
    "answers": [
      { "question": 1, "question_text": "How do you rate your work environment?", "rating": 5, "comment": "Excellent environment!" },
      { "question": 2, "question_text": "How do you rate team collaboration?", "rating": 4, "comment": "Good teamwork and collaboration" }
    ]
  }
]
```
## Fixtures & Initial Data

To load sample data for testing:

```bash
python manage.py loaddata feedback/fixtures/initial_data.json
```
