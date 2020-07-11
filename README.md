# Product_Index

This post introduces rest apis and graphql api for Product index app. Here have two rest apis and one graphql api for getting data. And also have a django admin panel for inserting data.

Aside from the Django application, this repo also includes the following:

* **queries.graphql** - an example of every query defined in the schema

## Setting up

Clone this repo, and in the directory follow these steps:

```bash
# Create virtual environment
python3.8 -m venv env
# Activate virtual environment
. env/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run DB migration
python manage.py migrate
# Run the application
python manage.py runserver
# Create superuser
python manage.py createsuperuser
# Collect static files for ckeditor
python manage.py collectstatic
```

## DB Connection
In this project, I have used mysql. so please follow these steps:
1. First you have to install mysql if you have not yet.
2. After installing mysql, please create a database and named it to product_index.
3. Now open the below file
```
/etc/mysql/my.cnf
```
And paste the following information bottom in the my.cnf file
```
[client]
database = product_brochure
user = your db user name
password = your db password
default-character-set = utf8
```
Save the file and close it.

## Create some data
1. Go to http://127.0.0.1:8000/admin/
2. Login with the created super user id
3. Create some data.

## Graphql API
1. Go to http://127.0.0.1:8000/graphql/, you'll be able to interact with the API there.
2. In project folder you will find a file named queries.graphql. In this file you will find some queries that you can use to check the API is working correctly or not.

## Rest API
1. http://127.0.0.1:8000/api/apps
    it will returns all apps list.
2. http://127.0.0.1:8000/api/app/id
    It will return an app and its related all value.