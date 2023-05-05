# HR API & Front-end

This is a simple Django-based API for an HR system

For front-end configurations [here](./templates/hr_frontend/README.md).


## Prerequisites

- Python 3.10
- PostgresSQL
## Setup

1. Clone the repository:

   ```
   git clone https://github.com/AshrafAlroomi/equevu-hr-task.git
   cd equevu-hr-task
   ```

2. Install the required packages using pip:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Configure the database:

   Update the `DATABASES` setting in the `settings/base.py` file (PostgreSQL or MySQL).

   For example, if you're using PostgreSQL, your `DATABASES` setting should look like:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'mydatabase',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

4. Apply the migrations:

   ```
   python manage.py migrate
   ```
   
## Running the API

1. Start the Django development server:

   ```
   python manage.py runserver
   ```

   The server will start running at `http://127.0.0.1:8000/`.

2. Access the API endpoints:

   - To register a candidate, send a POST request to `/api/v1/candidate/`.
   - To list candidates (admin access only), send a GET request to `/api/v1/candidates/`.
   - To download a candidate's resume (admin access only), send a GET request to `/api/v1/candidates/<candidate_id>/resume/`.
   - To list departments, send a GET request to `/api/v1/departments/`.

   To access admin-only endpoints, include the `X-ADMIN=1` header in the request.

## Running the tests

To run the tests, execute the following command:

```
python manage.py test
```

This command runs all the tests in the `tests.py` file.



