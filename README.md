# django_bucketlist
This is to implement an api using Django Rest Framework

## Installation and Setup
Clone the repo
```
https://github.com/valeria-chemtai/Checkpoint2-Bucketlist.git
```
Navigate to the root folder
```
cd checkpoint2-Bucketlist
```
create a virtualenv using virtualenvwrapper
```
mkvirtualenv django_bucketlist
```
activate virtualenv by running the following
```
workon django_bucketlist
```
Inside virtualenv open a postactivate file to store a script for  `database url` variables by running the command
```
subl $VIRTUAL_ENV/bin/postactivate
```
In the postactivate file add the following and replace the parenthesis in database_url with appropriate database owner name
```
export DATABASE_URL="postgres://{}@localhost:5432/django_bucketlist"
```
Alternatively if you do not want to automate the export of variables using postactivate, a simple export on the command line before running the app will work as follows:
```
$ export DATABASE_URL="postgres://{}@localhost:5432/django_bucketlist"
```

Install the requirements
```
pip install -r requirements.txt
```
Create a postgres database called django_bucketlist using PgAdmin, why? its easy

Alternatively create the database from the command line by running the script:
```
$ createdb django_bucketlist
```

Initialize, migrate, upgrade the datatbase
```
python manage.py makemigrations
python manage.py migrate
```
## Launch the progam
Run
```
python manage.py runserver
```