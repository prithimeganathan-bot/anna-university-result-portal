# Anna University Result Portal - Django Mimic

A web application that mimics the Anna University Controller of Examinations (COE) portal built using Django.

## Features
- Student login with Register Number and Date of Birth
- Institution / Staff login
- Student dashboard with tabs (Profile, Exam Schedule, Reg Preview, Assessment, Exam Results, Elective, Grievance)
- Institution dashboard with tabs (Home, Students, Hall Ticket, Attendance, Results, Fees, Grievance)
- Bulk student data upload via CSV/Excel
- Random captcha generation
- Django admin panel for data management

## Tech Stack
- Python 3.11
- Django 5.2
- SQLite3
- HTML / CSS / JavaScript

## Installation

1. Clone the repository
   git clone https://github.com/yourusername/anna-university-result-portal.git
   cd anna-university-result-portal

2. Create virtual environment
   python -m venv venv
   venv\Scripts\activate

3. Install dependencies
   pip install -r requirements.txt

4. Run migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create superuser
   python manage.py createsuperuser

6. Run server
   python manage.py runserver

7. Open browser
   http://127.0.0.1:8000/

## Student Login
- Go to http://127.0.0.1:8000/
- Enter Register Number and Date of Birth
- Click Login

## Admin Panel
- Go to http://127.0.0.1:8000/admin/
- Login with superuser credentials
- Add students and subject results