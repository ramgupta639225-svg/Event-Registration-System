# Event Registration System

A backend-focused Event Registration System built using **Django** and **Django REST Framework** as part of my **CodeAlpha Internship – Task 2**.

The system provides REST APIs to create and manage events, register users for events, view registrations, and cancel registrations.

## Features

* Event management
* Event list API
* Event detail API
* User registration for events
* User and event relationships
* View all registrations
* View registrations of a specific user
* Cancel event registration
* Duplicate registration prevention
* Event capacity validation
* Invalid user and event validation
* Django Admin Panel

## Technologies Used

* Python
* Django
* Django REST Framework
* SQLite
* Django ORM
* REST API
* Git & GitHub

## Project Structure

event_registration_system/
│
├── manage.py
│
├── event_registration_system/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── events/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── registrations/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py

## API Endpoints

### Events

| Method | Endpoint            | Description        |
| ------ | ------------------- | ------------------ |
| GET    | `/api/events/`      | View all events    |
| GET    | `/api/events/<id>/` | View event details |

### Registrations

| Method | Endpoint                          | Description                  |
| ------ | --------------------------------- | ---------------------------- |
| GET    | `/api/registrations/`             | View all registrations       |
| POST   | `/api/registrations/register/`    | Register a user for an event |
| GET    | `/api/registrations/user/<id>/`   | View user's registrations    |
| DELETE | `/api/registrations/<id>/cancel/` | Cancel a registration        |

## Registration Request

To register a user for an event:

json
{
    "user": 1,
    "event": 1
}


## Validation

The system checks:

* Whether the user exists
* Whether the event exists
* Whether the user is already registered
* Whether the event has reached its capacity
* Whether the registration exists before cancellation

## Database

This project uses **SQLite** with Django ORM for database management.

The main database models are:

* `User`
* `Event`
* `Registration`

The `Registration` model connects users with events using Django ForeignKey relationships.

## Project Purpose

This project was developed to practice:

* Django backend development
* Django REST Framework
* REST API development
* Database relationships
* Django ORM
* API validation
* CRUD operations
* Backend project structure

## Internship

**CodeAlpha Web Development Internship**

**Task:** Task 2 – Event Registration System

## Author

**Shardendu Prakash Gupta**

Python Backend Developer | Django | Flask | REST API
