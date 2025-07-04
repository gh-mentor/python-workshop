# Copilot Code Generation Instructions

## General Guidelines
- Use snake_case for variable and function names.
- Use PascalCase for class names.
- Use double quotes for strings.
- Ensure consistent indentation using 4 spaces.
- Use type hints for function arguments and return types.
- Use f-strings for string formatting.
- Handle exceptions using `try` and `except` blocks.
- Use context managers (e.g., `with` statements) for resource management.
- Write docstrings for all public functions and classes using the Google style.
- Avoid global variables; encapsulate functionality in classes or functions.
- Use list comprehensions and generator expressions where appropriate.
- Ensure all loops have proper termination conditions.
- Use descriptive names for variables and functions.
- Avoid deeply nested code; refactor into smaller functions if necessary.
- Follow PEP 8 for code style and PEP 257 for docstring conventions.

## Specific Instructions
- Use `const` for variables that do not change (use immutable types like tuples where applicable).
- Use lambda functions for anonymous functions.
- Use f-strings for string concatenation and formatting.
- Ensure all functions handle errors using exceptions.
- Verify that all imported modules are used.
- Check for proper error handling in all functions.
- Ensure all loops have proper termination conditions.
- Use descriptive names for variables and functions.
- Avoid deeply nested code; refactor into smaller functions if necessary.
- Check for any potential performance issues.

## Testing Guidelines
- Use pytest for all tests. [Reference](https://docs.pytest.org/)
- Ensure all tests are self-contained and do not rely on external state.
- Write tests for all public functions and classes.
- Ensure tests cover both typical and edge cases.
- Use descriptive names for test cases and functions.

### Example Test Snippet
```python
import pytest
from employee import Employee

def test_employee_creation():
    """Test the creation of an Employee object."""
    employee = Employee("Alice", 1, 75000.0, "Engineering")
    assert employee.name == "Alice"
    assert employee.id == 1
    assert employee.salary == 75000.0
    assert employee.department == "Engineering"
```

## Example Code Snippets

```python
# Good example of a function to add a new employee with proper naming and error handling
def add_employee(employee_name: str, employee_id: int) -> bool:
    """Adds a new employee to the company.

    Args:
        employee_name: The name of the employee.
        employee_id: The ID of the employee.

    Returns:
        True if the employee was added successfully, False otherwise.
    """
    try:
        # Assuming add_employee_to_database is a function that adds an employee to the database
        success = add_employee_to_database(employee_name, employee_id)
        if not success:
            raise ValueError("Failed to add employee to the database")
        return True
    except Exception as e:
        print(f"Failed to add employee: {e}")
        return False
```

```python
# Good example of a function to calculate the department budget with proper naming and error handling
def calculate_department_budget(department_id: str) -> float:
    """Calculates the budget for a department.

    Args:
        department_id: The ID of the department.

    Returns:
        The budget of the department.
    """
    try:
        # Assuming get_department_expenses and get_department_revenue are defined elsewhere
        expenses = get_department_expenses(department_id)
        revenue = get_department_revenue(department_id)
        return revenue - expenses
    except Exception as e:
        print(f"Failed to calculate department budget: {e}")
        raise
```

```python
# Good example of a function to fetch manager details with proper naming and error handling
def fetch_manager_details(manager_id: str) -> dict:
    """Fetches the details of a manager.

    Args:
        manager_id: The ID of the manager.

    Returns:
        A dictionary containing the details of the manager.
    """
    try:
        response = fetch(f"/api/managers/{manager_id}")
        if not response.ok:
            raise ValueError("Network response was not ok")
        return response.json()
    except Exception as e:
        print(f"Failed to fetch manager details: {e}")
        raise
```

```python
# Good example of a function to update an employee's department with proper naming and error handling
def update_employee_department(employee_id: int, new_department: str) -> bool:
    """Updates the department of an employee.

    Args:
        employee_id: The ID of the employee.
        new_department: The new department to be assigned.

    Returns:
        True if the department was updated successfully, False otherwise.
    """
    try:
        # Assuming update_department_in_database is defined elsewhere
        success = update_department_in_database(employee_id, new_department)
        if not success:
            raise ValueError("Failed to update employee department in the database")
        return True
    except Exception as e:
        print(f"Failed to update employee department: {e}")
        return False
```

```python
# Good example of a function to generate a report with proper string formatting using f-strings
def generate_employee_report(employee_id: int, employee_name: str, employee_salary: float) -> str:
    """Generates a report for an employee.

    Args:
        employee_id: The ID of the employee.
        employee_name: The name of the employee.
        employee_salary: The salary of the employee.

    Returns:
        A string containing the report of the employee.
    """
    return (
        f"Employee Report\n"
        f"ID: {employee_id}\n"
        f"Name: {employee_name}\n"
        f"Salary: {employee_salary}\n"
    )
```

