## Build:

You need: 
- Python3
- Poetry

```
poetry install
poetry shell
python manage.py createsuperuser
python manage.py makemigrations && python manage.py migrate
```

## Run:

`poetry run python manage.py runserver`
