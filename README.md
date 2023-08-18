# Docker-Django-DTL-app

git clone https://github.com/shreys7/django-todo.git

pip install virtualenv
python -m venv todo
todo\scripts\activate

cd django-todo
pip install django
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 
