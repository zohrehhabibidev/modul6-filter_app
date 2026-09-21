# Staff Filter App

A Django application for practicing database queries and filtering employees using the Django ORM.

## Project Description

This project was created as part of Module 6 of the Backend course.

The application works with employees and departments and demonstrates how to filter and query data using the Django ORM.

## Implemented Tasks

- Display all employees with their department and salary
- Find employees earning more than 3000 € per month
- Count employees earning 5000 € or more per month
- Calculate the average salary of employees in the Sales department
- Find employees hired before January 1, 2022 who are not in the HR department

## Technologies

- Python
- Django
- SQLite
- Django ORM

## Run the Project

Activate the virtual environment and install the requirements:

```bash
python -m pip install -r requirements.txt
```

Run the database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/employees/
```
