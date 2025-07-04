# Object-Relational Mapping (ORM) Exercise

In this exercise, you will use an Object-Relational Mapping (ORM) tool, specifically SQLAlchemy, to design and implement a database-backed Python application. The goal is to practice working with ORM tools to create, query, and manipulate database records efficiently while following best practices.

## Objectives

1. **Understand ORM Basics**: Learn how to map Python classes to database tables using SQLAlchemy.
2. **Database Design**: Define models with appropriate relationships (e.g., one-to-many, many-to-many).
3. **CRUD Operations**: Implement Create, Read, Update, and Delete operations using SQLAlchemy.
4. **Query Optimization**: Write optimized queries to fetch data efficiently.
5. **Error Handling**: Handle database-related exceptions gracefully.
6. **Testing**: Write unit tests using Python's built-in `unittest` module to validate the functionality of your application.
   - Ensure tests cover typical and edge cases.

## Requirements

1. **Setup**:
   - Use SQLAlchemy as the ORM tool.
   - Use SQLite as the database for simplicity.
   - Create a virtual environment and install the required dependencies.

2. **Database Models**:
   - Design a database schema for a simple application (e.g., a library system, employee management, or e-commerce).
   - Define at least three models with relationships (e.g., `User`, `Book`, `Loan` for a library system).

3. **CRUD Operations**:
   - Implement functions to:
     - Add new records to the database.
     - Retrieve records with filters (e.g., fetch all books borrowed by a specific user).
     - Update existing records.
     - Delete records.

4. **Query Optimization**:
   - Use SQLAlchemy's query features (e.g., joins, eager loading) to optimize data retrieval.

5. **Error Handling**:
   - Handle common database errors (e.g., integrity errors, connection issues) using try-except blocks.

6. **Testing**:
   - Write unit tests using Python's built-in `unittest` module to validate the functionality of your application.
   - Ensure tests cover typical and edge cases.

## Instructions

1. **Environment Setup**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install sqlalchemy
     ```

2. **Define Models**:
   - Create a `models.py` file and define your database models using SQLAlchemy's `Base` class.

3. **Implement CRUD Operations**:
   - Create a `database.py` file to implement functions for CRUD operations.

4. **Write Tests**:
   - Create a `tests/` directory and write unit tests for your application using the `unittest` module.
   - Example test structure:
     ```python
     import unittest
     from models import User, Book, Loan

     class TestLibrarySystem(unittest.TestCase):
         def test_add_user(self):
             """Test adding a new user to the database."""
             # ...test implementation...

         def test_fetch_books_by_user(self):
             """Test fetching all books borrowed by a specific user."""
             # ...test implementation...

         def test_update_book_title(self):
             """Test updating a book's title."""
             # ...test implementation...

         def test_delete_loan(self):
             """Test deleting a loan record."""
             # ...test implementation...

     if __name__ == "__main__":
         unittest.main()
     ```

5. **Run the Application**:
   - Use a script (e.g., `app.py`) to demonstrate the functionality of your application.

6. **Run Tests**:
   - Run tests using the `unittest` module:
     ```bash
     python -m unittest discover tests
     ```

## Recommended Folder Structure

Organize your project using the following folder structure for better maintainability and clarity:

```
ex5-orm/
├── app.py               # Main application script
├── database.py          # Database connection and CRUD operations
├── models.py            # SQLAlchemy models
├── tests/               # Unit tests
│   ├── __init__.py      # Makes the tests directory a package
│   ├── test_models.py   # Tests for models
│   ├── test_database.py # Tests for CRUD operations
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
```

### Description of Key Files and Directories

- **`app.py`**: Contains the main script to demonstrate the functionality of the application.
- **`database.py`**: Implements database connection and CRUD operations.
- **`models.py`**: Defines the SQLAlchemy models for the application.
- **`tests/`**: Contains unit tests for the application.
  - **`test_models.py`**: Tests for the SQLAlchemy models.
  - **`test_database.py`**: Tests for CRUD operations and database interactions.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`README.md`**: Provides documentation for the project, including objectives, instructions, and folder structure.

## Sample Prompts for Copilot Assistance

Here are some sample prompts you can use with Copilot to guide you through the design, implementation, and testing phases of this exercise. These prompts will help you leverage Copilot effectively while following the provided coding instructions.

### Design Phase
1. **Model Creation**:
   - "Generate a SQLAlchemy model for a User with fields id, name, and email, following PEP 8 conventions."
   - "Create a SQLAlchemy model for a Book with fields id, title, and author, and include a relationship to a Loan model."
   - "Define a Loan model with relationships to User and Book models using SQLAlchemy."

2. **Database Schema**:
   - "Write a function to initialize the database schema using SQLAlchemy's `Base.metadata.create_all`."

### Implementation Phase
1. **CRUD Operations**:
   - "Write a function to add a new user to the database using SQLAlchemy, with proper error handling."
   - "Generate a function to retrieve all books borrowed by a specific user using SQLAlchemy queries."
   - "Create a function to update a book's title in the database, ensuring it handles exceptions gracefully."
   - "Write a function to delete a loan record from the database using SQLAlchemy."

2. **Query Optimization**:
   - "Generate an optimized query to fetch all loans with user and book details using eager loading in SQLAlchemy."
   - "Write a query to count the number of books borrowed by each user using SQLAlchemy's aggregation functions."

3. **Error Handling**:
   - "Write a try-except block to handle integrity errors when adding a new user to the database."

### Testing Phase
1. **Unit Tests**:
   - "Write a unittest test case to verify that a new user can be added to the database."
   - "Generate a unittest test to check that a book can be retrieved by its title."
   - "Write a test case to ensure that deleting a loan record removes it from the database."

2. **Edge Cases**:
   - "Write a test to handle the case where a user tries to borrow a book that does not exist."
   - "Generate a test to verify that duplicate email addresses cannot be added to the User table."

3. **Mocking and Isolation**:
   - "Write a unittest test that mocks the database session to test the add_user function in isolation."

### Demonstration Phase
1. **Application Script**:
   - "Generate a script to demonstrate adding a user, a book, and a loan, and then retrieving all loans for a specific user."
   - "Write a script to showcase updating a book's title and deleting a loan record."

2. **Logging and Output**:
   - "Add logging to the application script to display success or failure messages for each operation."

### General Tips
- Use prompts like "Refactor this function to improve readability and follow PEP 8 guidelines."
- If Copilot's suggestions are not precise, refine your prompt by including more details, such as "Generate a SQLAlchemy model with a one-to-many relationship between User and Loan."

By using these prompts, you can efficiently complete the exercise while adhering to best practices and the provided coding instructions. Happy coding!