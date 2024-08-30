# Project Overview
This Django project has two REST API endpoints that provide information about Banks and its branches.



## Setup Instructions

### 1. Clone the Repository
```bash
gh repo clone niraj2099M/bankapi
cd bankapi/

```

### 2. Install Dependencies
Create a virtual environment and install the required Python packages:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Set environment variables: Add a .env file and add the following
- DB_ID: Your database userid
- DB_PASS: Your database password

### 4. Django Setup
Migrate the database:
```bash
python manage.py makemigrations
python manage.py migrate
```
Load data from sql file to Postgresql Database:
```bash
psql -U user -h 127.0.0.1 -d data_base < your_sql_file.sql

```


## Running the Application

Start the Django development server:
```bash
python3 manage.py runserver
```

## API Endpoints
- GET http://127.0.0.1:8000/banks >> list of all banks
- POST http://127.0.0.1:8000/branch >> details of a branch
    - request body
    ```
        {
          "ifsc": "IFSC CODE"
        }
    ```
