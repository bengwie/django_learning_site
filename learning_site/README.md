pip install django

jango-admin startproject learening_site

python manage.py runserver 0.0.0.0:8000
—— Then go to browser to open http://localhost:8000 to see the app

python manage.py startapp courses

jhidayat-a01:learning_site jhidayat$ python manage.py makemigrations courses
Migrations for 'courses':
  courses/migrations/0001_initial.py
    - Create model Course

    jhidayat-a01:learning_site jhidayat$ python manage.py shell
    Python 2.7.14 |Anaconda, Inc.| (default, Dec  7 2017, 11:07:58)
    Type "copyright", "credits" or "license" for more information.

    IPython 5.4.1 -- An enhanced Interactive Python.
    ?         -> Introduction and overview of IPython's features.
    %quickref -> Quick reference.
    help      -> Python's own help system.
    object?   -> Details about 'object', use 'object??' for extra details.

    In [1]:

    In [1]: from courses.models import Course

    In [2]: Course.objects.all()
    Out[2]: <QuerySet []>

    In [3]: type(Course.objects.all())
    Out[3]: django.db.models.query.QuerySet

    In [4]: c = Course()

    In [5]: c.title = "Python Basics"

    In [6]: c.description = "Learn the basics of Python"

    In [7]: c.save()

    In [8]: Course.objects.all()
    Out[8]: <QuerySet [<Course: Course object>]>
