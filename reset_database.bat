del users\migrations\0001_initial.py
del companies\migrations\0001_initial.py
del calls\migrations\0001_initial.py

del users\migrations\__pycache__\*.pyc
del companies\migrations\__pycache__\*.pyc
del calls\migrations\__pycache__\*.pyc

del db.sqlite3

python manage.py makemigrations users
python manage.py makemigrations companies
python manage.py makemigrations calls



python manage.py migrate

python manage.py createsuperuser

