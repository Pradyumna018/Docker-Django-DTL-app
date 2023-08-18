# Docker-Django-DTL-app

git clone https://github.com/Pradyumna018/Docker-Django-DTL-app.git

pip install virtualenv

python -m venv DtlDjango

DtlDjango\scripts\activate

cd Docker-Django-DTL-app

pip install django

python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 
