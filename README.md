# Parallel-Project (Django-Python)
This is a project for the parallel and distributed system course where we make ARTwithHEART online platform developed to cater to artists and art enthusiasts
## Project Setup Instructions:
 ### Prerequisites
Python 3.x: Make sure Python is installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

PostgreSQL: Install PostgreSQL to set up the project's database. You can download it from the official PostgreSQL website: https://www.postgresql.org/download/

 It's recommended to use Visual Studio Code as the IDE for this project. You can download it from the official website: https://code.visualstudio.com/

### Installation on Windows:
1-Clone this Repo




2-Open folder parallelprj from VS code




3-Install the project dependencies:

```
pip install -r requirements.txt

```

4- Database Configuration:

Open the ```settings.py``` file located in the project's root directory.


Modify the database configuration according to your PostgreSQL setup. Update the DATABASES section with your database credentials.



5-Apply database migrations:
```
python manage.py migrate
```

6-run server:

```
python manage.py runserver

```
7- Open a web browser and visit http://localhost:8000 to access the application.

## Accessing the Admin Interface:
1-Start the development server if it's not already running:
```
python manage.py runserver
```
2-Open a web browser and visit http://localhost:8000/admin.
