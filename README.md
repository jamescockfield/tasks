Django REST / React app for a task management system

Setup
-----
/frontend
    Copy `.env.example` to `.env.local` and adjust as needed
/backend
    `python manage.py migrate`
    `python manage.py createsuperuser`

Running
-------
`cd backend && python manage.py runserver`
`cd frontend && npm run dev`