# To-Do Application in Django with PostgreSQL
To-Do application using Django Web Framework. As database used PostgreSQL.

## Installation
Install pip:
```bash
pyhton get-pip.py
```
Install Django framework:
```
pip install Django
```
Install Psycopg2:
```
pip install psycopg2
```
Create database in PostgreSQL.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost'
    }
}
```
Then you can just migrate all models by commands like:
```bash
python manage.py makemigrations todos
```
```
python manage.py sqlmigrate todos 0001
```
```
python manage.py migrate
```
## Usage
Run this code and follow the link http://127.0.0.1:8000/
## Examples
### Add a new item, after it is stored in the database:

![image](https://sun9-25.userapi.com/impg/vUrAkyC8OreJOb0kmkTdQesTb94EF9RSUxuRcQ/I3BA0WgSFOU.jpg?size=1920x1080&quality=96&sign=c087cb9a1e9259354e991519388c223f&type=album)

### After adding, you can remove them after you complete:

![image](https://sun9-31.userapi.com/impg/eRoFWEQK6KHN0B87M2EC2eQKN-1KYdhnW9t22A/m6hiWSQMgcQ.jpg?size=1920x1080&quality=96&sign=ca64322b9fd00b40ebb3dac9b9d33e31&type=album)

### This is what the database and content looks like:

![image](https://sun9-4.userapi.com/impg/cPFOXTahZs58ae6-t9hRMESMzzeh0jO0Rh9xyg/UOgok62Ifew.jpg?size=738x775&quality=96&sign=af67dae82e02b13963294c04a1d12945&type=album)

## License
[MIT](https://choosealicense.com/licenses/mit/)
