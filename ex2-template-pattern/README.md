# Template Method Pattern Exercise

In this exercise, you will implement and enhance an application that uses the Template Method Pattern. The goal is to understand the pattern, refactor the project to follow best practices, and adhere to SOLID design principles.

## Objectives

1. **Understand the Template Method Pattern**: Learn how the pattern works and its use cases.
2. **Refactor Project Structure**: Organize the project to follow Python best practices.
3. **Adhere to SOLID Principles**: Refactor the code to ensure it adheres to SOLID design principles.
4. **Separate Contracts from Implementation**: Use interfaces to decouple contracts from their implementations.
5. **Dependency Injection**: Decouple classes to improve testability.
6. **Unit Testing**: Write unit tests to validate the functionality of the application.

## Requirements

1. **Suggested Project Structure**:
   - Following is the suggested folder structure:
     ```
     ex2-template-pattern/
     ├── src/
     │   ├── reports/
     │   │   ├── __init__.py
     │   │   ├── i_report_template.py
     │   │   ├── company_report.py
     │   ├── __init__.py
     │   ├── main.py
     ├── tests/
     │   ├── __init__.py
     │   ├── test_company_report.py
     ├── requirements.txt
     ├── README.md
     ├── .gitignore
     └── .env
     ```


## Instructions

1. **Refactor Project Structure**:
   - Organize the project into the suggested folder structure.
   - Separate interfaces into their own modules.

2. **Implement Dependency Injection**:
   - Refactor classes to use dependency injection for improved testability.

3. **Write Unit Tests**:
   - Create a `tests/` directory and write unit tests for all public classes and functions.

4. **Run Tests**:
   - Use `pytest` to run the tests:
     ```bash
     pytest
     ```

5. **Documentation**:
   - Explain the Template Method Pattern and how it is used in the application.

## Sample Prompts for Copilot Assistance

Here are some sample prompts you can use with Copilot to guide you through the refactoring and testing phases of this exercise:

### Refactoring Phase
1. **Interface Creation**:
   - "Generate an interface for a report template with methods for generating headers, footers, and content."
   - "Create a class that implements the report template interface for a company report."

2. **Dependency Injection**:
   - "Refactor the `CompanyReport` class to accept a dependency for data retrieval."

3. **SOLID Principles**:
   - "Refactor the code to ensure the Single Responsibility Principle is followed."

### Testing Phase
1. **Unit Tests**:
   - "Write a unit test case to verify that the `CompanyReport` class generates a report correctly."
   - "Generate a unit test to check that the header and footer methods are called in the correct order."

2. **Mocking and Isolation**:
   - "Write a unit test that mocks the data retrieval dependency for the `CompanyReport` class."

### Documentation Phase
1. **Explain the Pattern**:
   - "Write a section in the README to explain the Template Method Pattern with examples."
   - "Add a diagram to illustrate the flow of the Template Method Pattern."

By following these instructions and using the provided prompts, you can refactor the project to adhere to best practices and ensure it is well-documented and testable. Happy coding!
