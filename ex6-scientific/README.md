# Scientific Computing with Python Exercise

In this exercise, you will explore Python's capabilities for scientific applications while leveraging GitHub Copilot to accelerate development and reduce complexity. You will use advanced Python features, such as decorators, context managers, and asynchronous programming with `asyncio`, to implement solutions for scientific problems. The goal is to practice writing efficient, maintainable, and scalable code while utilizing Copilot to simplify implementation and reduce errors.

## Objectives

1. **Learn Advanced Python Features**: Understand and apply advanced Python features such as decorators, context managers, and asynchronous programming.
2. **Scientific Problem Solving**: Solve scientific problems using Python libraries such as `numpy`, `scipy`, and `matplotlib`.
3. **Code Optimization**: Write efficient and optimized code for computational tasks.
4. **Error Handling**: Handle exceptions gracefully to ensure robust applications.
5. **Testing**: Write unit tests to validate the functionality of your scientific solutions.

## Requirements

1. **Setup**:
   - Use Python 3.8 or later.
   - Create a virtual environment and install the required dependencies.

2. **Scientific Libraries**:
   - Use libraries such as `numpy`, `scipy`, `matplotlib`, and `asyncio` for computations, visualizations, and asynchronous tasks.

3. **Advanced Python Features**:
   - Implement and use decorators to enhance the functionality of functions.
   - Use context managers to manage resources efficiently.
   - Use `asyncio` to implement asynchronous tasks for scientific computations.

4. **Problem Solving**:
   - Solve at least three scientific problems, such as:
     - Numerical integration or differentiation.
     - Solving systems of linear equations.
     - Simulating physical systems (e.g., pendulum motion or population dynamics).
     - Data visualization for scientific datasets.

5. **Error Handling**:
   - Handle common errors (e.g., invalid inputs, numerical instability) using `try` and `except` blocks.

6. **Testing**:
   - Write unit tests using Python's built-in `unittest` module to validate your solutions.
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
     pip install numpy scipy matplotlib asyncio
     ```

2. **Implement Solutions**:
   - Create a `solutions.py` file to implement your scientific solutions.
   - Use Copilot to assist in generating boilerplate code and implementing complex logic. For example:
     - "Write a function to solve a system of linear equations using `numpy.linalg.solve`."
     - "Generate a decorator to measure the execution time of a function."

3. **Visualize Results**:
   - Use `matplotlib` to create visualizations for your solutions.
   - Use Copilot to assist in generating plots. For example:
     - "Generate a line plot for a sine wave using `matplotlib`."

4. **Asynchronous Programming**:
   - Use `asyncio` to implement asynchronous tasks for computational problems.
   - Use Copilot to assist in writing asynchronous functions. For example:
     - "Write an asynchronous function to compute the sum of squares for a large dataset."

5. **Write Tests**:
   - Create a `tests/` directory and write unit tests for your solutions using the `unittest` module.
   - Example test structure:
     ```python
     import unittest
     from solutions import solve_linear_system, numerical_integration

     class TestScientificSolutions(unittest.TestCase):
         def test_solve_linear_system(self):
             """Test solving a system of linear equations."""
             # ...test implementation...

         def test_numerical_integration(self):
             """Test numerical integration using the trapezoidal rule."""
             # ...test implementation...

         def test_invalid_input(self):
             """Test handling of invalid inputs."""
             # ...test implementation...

     if __name__ == "__main__":
         unittest.main()
     ```

6. **Run Tests**:
   - Run tests using the `unittest` module:
     ```bash
     python -m unittest discover tests
     ```

## Recommended Folder Structure

Organize your project using the following folder structure for better maintainability and clarity:

```
ex6-scientific/
├── async_tasks.py       # Asynchronous tasks for scientific computations
├── solutions.py         # Implementation of scientific solutions
├── visualizations.py    # Visualization scripts using matplotlib
├── tests/               # Unit tests
│   ├── __init__.py      # Makes the tests directory a package
│   ├── test_solutions.py # Tests for solutions.py
│   ├── test_async.py    # Tests for async_tasks.py
├── requirements.txt     # List of dependencies
├── README.md            # Project documentation
```

### Description of Key Files and Directories

- **`async_tasks.py`**: Contains asynchronous tasks implemented using `asyncio`.
- **`solutions.py`**: Implements the core scientific solutions.
- **`visualizations.py`**: Contains scripts for generating visualizations using `matplotlib`.
- **`tests/`**: Contains unit tests for the application.
  - **`test_solutions.py`**: Tests for the functions in `solutions.py`.
  - **`test_async.py`**: Tests for the asynchronous tasks in `async_tasks.py`.
- **`requirements.txt`**: Lists all the dependencies required for the project.
- **`README.md`**: Provides documentation for the project, including objectives, instructions, and folder structure.

## Sample Prompts for Copilot Assistance

Here are some sample prompts you can use with Copilot to guide you through the exercise:

### Design Phase
1. **Function Implementation**:
   - "Write a function to compute the numerical integration of a function using the trapezoidal rule."
   - "Generate a function to solve a quadratic equation using the quadratic formula."

2. **Decorator Creation**:
   - "Write a decorator to log the execution time of a function."
   - "Generate a decorator to cache the results of a function."

3. **Context Manager**:
   - "Write a context manager to handle file operations safely."
   - "Generate a context manager to manage a temporary directory."

### Implementation Phase
1. **Asynchronous Programming**:
   - "Write an asynchronous function to fetch data from multiple sources using `asyncio.gather`."
   - "Generate an asynchronous task to compute the factorial of a number."

2. **Visualization**:
   - "Generate a scatter plot for random data points using `matplotlib`."
   - "Write a function to create a heatmap for a 2D array using `matplotlib`."

3. **Error Handling**:
   - "Write a try-except block to handle division by zero in a numerical computation."
   - "Generate error handling for invalid inputs in a function."

### Testing Phase
1. **Unit Tests**:
   - "Write a unittest test case to validate the numerical integration function."
   - "Generate a unittest test to check the solution of a quadratic equation."

2. **Edge Cases**:
   - "Write a test to handle the case where the input array is empty."
   - "Generate a test to verify the behavior of a function with extremely large inputs."

3. **Mocking and Isolation**:
   - "Write a unittest test that mocks a file operation in a context manager."

### General Tips
- Use prompts like "Refactor this function to improve readability and follow PEP 8 guidelines."
- If Copilot's suggestions are not precise, refine your prompt by including more details, such as "Generate a function to compute the eigenvalues of a matrix using `numpy.linalg.eig`."

## Deliverables

1. A Python application with:
   - Implemented solutions in `solutions.py`.
   - Visualizations in `visualizations.py`.
   - Asynchronous tasks in `async_tasks.py`.
   - Unit tests in the `tests/` directory.

2. A `requirements.txt` file listing all dependencies.

3. A README.md file documenting how to set up and run the application.

