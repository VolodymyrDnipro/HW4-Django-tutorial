## HW4-Django-tutorial

1. Run server
```bash
python manage.py runserver
```

2. Run Celery
```bash
celery -A mysite worker -l info
```
3. Get info
```bash
celery -A mysite inspect active
```
# DB
1. Make Migrations
```bash
python manage.py makemigrations
```
2. Migrate
```bash
python manage.py migrate
```
