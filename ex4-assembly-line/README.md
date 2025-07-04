# Assembly Line Simulation

In this exercise, you will implement all methods of the `FactoryAssemblyLine` class. The `FactoryAssemblyLine` class is a minimal simulation of an assembly line in a factory. The goal is to implement the class so that all provided tests pass successfully.

## Objectives

1. **Understand Class Design**: Learn how to design and implement a class with multiple methods.
2. **Simulation Logic**: Implement the logic for simulating an assembly line.
3. **Error Handling**: Ensure proper error handling in all methods.
4. **Testing**: Validate your implementation using the provided test cases.

## Requirements

1. **Setup**:
   - Use Python 3.8 or later.
   - Install any required dependencies (if applicable).

2. **Class Implementation**:
   - Implement the `FactoryAssemblyLine` class with all required methods.
   - Ensure the class adheres to the principles of object-oriented programming.

3. **Error Handling**:
   - Handle exceptions gracefully using `try` and `except` blocks.

4. **Testing**:
   - Use the provided test cases in the `tests` folder to validate your implementation.
   - Ensure all tests pass successfully.

## Instructions

1. **Environment Setup**:
   - Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies (if any):
     ```bash
     pip install -r requirements.txt
     ```

2. **Class Implementation**:
   - Open the `factory_assembly_line.py` file.
   - Implement all methods of the `FactoryAssemblyLine` class.

3. **Run Tests**:
   - Navigate to the `tests` folder and run the tests:
     ```bash
     python -m unittest discover
     ```

4. **Debugging**:
   - If any tests fail, debug your implementation and fix the issues.

## Recommended Folder Structure

To maintain a clean and organized project, use the following folder structure:

```
repo/
│
├── ex4-assembly-line/
│   ├── factory_assembly_line.py   # Implementation of the FactoryAssemblyLine class
│   ├── tests/                     # Folder containing all test cases
│   │   ├── test_factory_assembly_line.py  # Unit tests for the FactoryAssemblyLine class
│   ├── README.md                  # Documentation for the exercise
│   ├── requirements.txt           # List of dependencies (if any)
│
├── other-exercises/               # Other exercises in the workshop
```

This structure ensures that the implementation, tests, and documentation are clearly separated, making the project easier to navigate and maintain.

## Example Prompts for Copilot Assistance

Here are some sample prompts you can use with Copilot to guide you through the implementation and testing phases of this exercise:

### Implementation Phase
1. **Method Implementation**:
   - "Write a method to add a new item to the assembly line queue."
   - "Generate a method to process the next item in the assembly line."
   - "Create a method to calculate the total processing time for all items in the queue."

2. **Error Handling**:
   - "Write a try-except block to handle cases where the assembly line queue is empty."

3. **Optimization**:
   - "Refactor the method to improve its performance when processing large queues."

### Testing Phase
1. **Unit Tests**:
   - "Write a `unittest` test case to verify that an item can be added to the assembly line queue."
   - "Generate a `unittest` test to check that processing an item reduces the queue size."
   - "Write a test case to ensure that an exception is raised when trying to process an empty queue."

2. **Edge Cases**:
   - "Write a test to handle the case where the assembly line queue is initialized with no items."
   - "Generate a test to verify that the total processing time is zero for an empty queue."

By following these instructions and leveraging Copilot effectively, you can complete the exercise and ensure all tests pass successfully. Happy coding!

