# community-website
dsc community website

# Requirements
1. docker
2. docker-compose
3. linux/macos recommended

# Steps to install
1. clone the repository
2. go to the root directory
3. in terminal write ```docker-compose build```
4. ```docker-compose up```

# initial db setup
1. open a new terminal while the docker is still running
2. ```docker-compose exec api sh -c "python manage.py makemigrations"```
3. ```docker-compose exec api sh -c "python manage.py migrate"```
### To create a superuser in db
1.  ```docker-compose exec api sh -c "python manage.py createsuperuser"```

# Seeding db with fake data
1. docker-compose exec api python manage.py seed <django_app_name>   

# React app
1. go to  ```localhost:3000```

# django app
1. go to ```localhost:8000```
