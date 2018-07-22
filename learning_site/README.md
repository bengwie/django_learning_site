pip install django

jango-admin startproject learening_site

python manage.py runserver 0.0.0.0:8000
—— Then go to browser to open http://localhost:8000 to see the app

python manage.py startapp courses

jhidayat-a01:learning_site jhidayat$ python manage.py makemigrations courses
Migrations for 'courses':
  courses/migrations/0001_initial.py
    - Create model Course
