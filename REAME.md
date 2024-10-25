# Library Checkout System

This project is a Library Checkout System built using FastAPI and SQLAlchemy. It allows users to manage authors, books, and checkouts through a RESTful API.

## Project Structure

```
alembic/
	env.py
	script.py.mako
alembic.ini
app/
	__init__.py
	database.py
	main.py
	models/
		__init__.py
		author.py
		book.py
		checkout.py
	routers/
		__init__.py
		author.py
		book.py
		checkout.py
	schemas/
		__init__.py
		author.py
		book.py
		checkout.py
requirements.txt
```

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a virtual environment and activate it:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the database migrations:**

    ```sh
    alembic upgrade head
    ```

## Running the Application

1. **Start the FastAPI server:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## Project Modules

### Models

- 

author.py

: Defines the [`Author`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmacbookpro%2FDesktop%2FCOPILOT%20TRAINING%2Flibrary-checkout%2Fapp%2Frouters%2Fauthor.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A57%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmacbookpro%2FDesktop%2FCOPILOT%20TRAINING%2Flibrary-checkout%2Fapp%2Fschemas%2Fauthor.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A12%2C%22character%22%3A6%7D%7D%5D%2C%223782e651-cf6a-4a15-9231-29ef79cad4c0%22%5D "Go to definition") model.
- 

book.py

: Defines the `Book` model.
- 

checkout.py

: Defines the `Checkout` model.

### Schemas

- 

author.py

: Defines the Pydantic schemas for [`Author`](command:_github.copilot.openSymbolFromReferences?%5B%22%22%2C%5B%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmacbookpro%2FDesktop%2FCOPILOT%20TRAINING%2Flibrary-checkout%2Fapp%2Frouters%2Fauthor.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A2%2C%22character%22%3A57%7D%7D%2C%7B%22uri%22%3A%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2FUsers%2Fmacbookpro%2FDesktop%2FCOPILOT%20TRAINING%2Flibrary-checkout%2Fapp%2Fschemas%2Fauthor.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%22pos%22%3A%7B%22line%22%3A12%2C%22character%22%3A6%7D%7D%5D%2C%223782e651-cf6a-4a15-9231-29ef79cad4c0%22%5D "Go to definition").
- 

book.py

: Defines the Pydantic schemas for `Book`.
- 

checkout.py

: Defines the Pydantic schemas for `Checkout`.

### Routers

- 

author.py

: Contains the API routes for managing authors.
- 

book.py

: Contains the API routes for managing books.
- 

checkout.py

: Contains the API routes for managing checkouts.
- 

__init__.py

: Initializes the routers package and includes the individual routers.

### Database

- 

database.py

: Contains the database connection and session management.

### Main Application

- 

main.py

: The entry point of the application. It includes the routers and creates the database tables.

### Alembic

- 

env.py

: Alembic environment configuration file.
- 

alembic.ini

: Alembic configuration file.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or inquiries, please contact [your-email@example.com](mailto:your-email@example.com).