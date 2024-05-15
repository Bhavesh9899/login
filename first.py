#first of all create virtual environment
#   run command : python -m venv myVenv
#   then activate(run) : myVenv\Scripts\activate
#   then install : pip install django
#   then create project : Django-admin startproject myproject .
#   then create application : python manage.py startapp myApp

#to run the project
#   myVenv\Scripts\activate
#   python manage.py migrate
#   python manage.py runserver

#after creating model
#   python manage.py makemigrations
#   python manage.py migrate
#   python manage.py runserver

# database 
#   pip install --only-binary :all: mysqlclient