# backend-challenge-py
 Backend Developer Challenge - Darwin Interactive | Pedro Leal

This repository offers a version of the challenge solution that takes a more complex approach to accomplishing the task compared to first version, along with a more detailed perspective.

Project setup:
$ mkdir currency_exchange_api
cd currency_exchange_api
python -m venv venv
source venv/bin/activate
pip install fastapi uvicorn sqlalchemy pydantic requests httpx aioredis fastapi

Project Structure:
currency_rate_project/
├── currency_rate/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── utils.py
├── logs/
│   └── exchange_rate.log
├── run.py
└── venv/
    ├── Scripts/
    └── ...

Here's a brief description of each file:

currency_rate/ directory: Contains the core application code.

__init__.py: Makes the directory a Python package.

crud.py: Contains the database interaction logic.

database.py: Sets up the database connection.

dependencies.py: Defines dependencies for the FastAPI application.

main.py: The main entry point for the FastAPI application.

models.py: Defines the database models.

schemas.py: Defines the Pydantic schemas for request and response models.

utils.py: Contains utility functions, including those for fetching data from the Frankfurter API.

logs/ directory: Stores log files.

exchange_rate.log: Log file for API responses and other logs.

run.py: Entry point for running the application using Uvicorn.

venv/: The virtual environment directory (created using python -m venv venv).

To run the application, navigate to the currency_rate_project directory and use the following command: python run.py
