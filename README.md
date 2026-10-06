# Student Task Manager

**FDS Django Practical Project**  
**Student:** Sifat Kaur  
**Registration No.:** RA2511056030006  
**Course:** B.Tech CSE (Data Science) - 2nd Year

## Project

This is a simple Task Manager made using Django. I selected the **ToDo web application** idea from the GeeksforGeeks Django Projects list and developed a basic version for my FDS practical.

Reference: https://www.geeksforgeeks.org/python/django-projects/

## Features

- Add a task
- Edit a task
- Mark a task as completed
- Delete a task
- Search tasks by title
- Filter pending and completed tasks
- Set task priority
- Add a due date
- View total, pending and completed task counts

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```text
student_todo_django/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── run_project.bat
├── student_todo/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __init__.py
└── tasks/
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── models.py
    ├── urls.py
    ├── views.py
    ├── tests.py
    ├── management/commands/seed_data.py
    ├── static/tasks/style.css
    └── templates/tasks/
        ├── base.html
        ├── task_list.html
        └── task_form.html
```

## How to Run

### 1. Create a virtual environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py migrate
```

### 4. Add sample tasks

```bash
python manage.py seed_data
```

### 5. Start the server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in the browser.

## How It Works

The project follows Django's MVT structure.

- **Model:** `tasks/models.py` stores the task information in the database.
- **View:** `tasks/views.py` handles adding, editing, completing and deleting tasks.
- **Template:** HTML files display the tasks and forms.
- **URL:** `tasks/urls.py` connects URLs to the required views.
- **Form:** `TaskForm` is used to take and validate task details.
- **Database:** SQLite is used to store the data.

The main task fields are title, description, priority, due date, completion status and creation time.

## Basic Demo

1. Start the Django server.
2. Show the sample tasks on the home page.
3. Add a new task.
4. Edit the task.
5. Mark it as completed.
6. Use the search and status filter.
7. Delete the task.

## GitHub

The repository should contain the Django project files and `README.md`.

Do not upload the virtual environment, `db.sqlite3`, or generated `__pycache__` folders.
