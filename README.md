# Library Management System

This is a Library Management System built with FastAPI and SQLAlchemy.

## Project Structure
# Library Management System

This is a Library Management System built with FastAPI and SQLAlchemy.

## Project Structure


## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```sh
    alembic upgrade head
    ```

## Running the Application

To run the application, use the following command:
```sh
uvicorn app.main:app --reload