## Build:

You need: 
- Python3
- Poetry

```
poetry shell
poetry install
python manage.py makemigrations && python manage.py migrate
python manage.py createsuperuser
```

## Run:

```
poetry shell
python manage.py runserver
```

## Package to one executable:

```
pyinstaller --name=canicrossy --onefile --noconfirm start-app.py
```



