## Build:

You need: 
- Python3
- Poetry

```
poetry shell
poetry install
python manage.py createsuperuser
python manage.py makemigrations && python manage.py migrate
```

## Run:

```
poetry shell
python manage.py runserver
```
