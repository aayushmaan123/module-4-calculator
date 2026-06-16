# Module 4: Advanced Object-Oriented Programming (OOP) and Comprehensive Testing in Python

## Module Overview
Welcome to **Module 4**, where you will elevate your Python programming skills by delving deeper into **Object-Oriented Programming (OOP)** and mastering **comprehensive testing techniques** using `pytest`. Building upon your foundational knowledge from previous modules, this module introduces more sophisticated OOP concepts and emphasizes the importance of achieving complete test coverage to ensure code reliability and quality.

Your primary textbook for this module is the provided codebase, organized with the following folder structure:

```
app/
├── calculator/
│   └── __init__.py
├── calculation/
│   └── __init__.py
├── operation/
│   └── __init__.py
tests/
├── test_calculations.py
├── test_calculator.py
└── test_operations.py
```

Each `__init__.py` file within the `app/` subdirectories contains the relevant code for that module. The `tests/` directory includes unit and parameterized tests to verify the functionality of your application.

By studying and interacting with this code, you'll gain hands-on experience in implementing advanced OOP principles, designing robust command-line interfaces, applying the DRY (Don't Repeat Yourself) principle, handling errors gracefully, and ensuring code reliability through thorough testing.

## Why Advanced OOP and Comprehensive Testing?
**Object-Oriented Programming (OOP)** is a cornerstone of modern software development, enabling developers to create modular, reusable, and scalable code. By leveraging advanced OOP concepts such as inheritance, encapsulation, and polymorphism, you can design more sophisticated applications that are easier to maintain and extend.

**Comprehensive Testing** is essential for ensuring the reliability and correctness of your applications. Utilizing testing frameworks like `pytest` allows you to write extensive unit and parameterized tests, achieving high test coverage that guarantees all parts of your code are functioning as intended. Striving for **100% test coverage** minimizes the risk of hidden bugs and enhances overall code quality.

## Learning Outcomes
By the end of this module, you will be able to:
- CLO 6: Implement object-oriented programming principles in Python.
- CLO 7: Apply professional terminology and concepts related to web systems development.

## Module 4 Learning Pathway

### Recall

**Title:** Reflecting on Your OOP and Testing Experiences  
**Grading Type:** Points  
**Instructions:** 
- **Discussion Forum:** Share your experiences with Object-Oriented Programming and testing in Python.
  - Discuss any projects where you applied OOP principles.
  - Reflect on the challenges you faced while writing tests and achieving test coverage.
- **Quiz:** Complete a short quiz to assess your current understanding of advanced OOP concepts and testing methodologies.
- **Purpose:** This activity will help you recall and articulate your prior experiences, setting the stage for deeper learning in this module.

### Read

Your **primary textbook** for this module is the provided codebase. Each `__init__.py` file within the `app/` subdirectories is thoroughly commented to explain advanced OOP concepts, error handling strategies, and testing best practices. Here’s an overview of the key components:

1. **`app/calculator/__init__.py`**
   - **Purpose:** Implements a professional-grade calculator using Python’s REPL (Read-Eval-Print Loop) pattern.
   - **Key Concepts:** 
     - Advanced control structures (`while` loops, `if-elif-else` statements)
     - User input handling
     - Comprehensive error handling using `try-except` blocks
     - Modular code organization by importing from `operation.py` and `calculation.py`
     - Demonstrates OOP paradigms: LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission)

2. **`app/operation/__init__.py`**
   - **Purpose:** Contains the `Operation` class with static methods for basic arithmetic operations.
   - **Key Concepts:**
     - **Classes and Static Methods:** Encapsulate related functionalities within a class using static methods.
     - **Encapsulation and Abstraction:** Group related functions together to enhance code organization and reusability.
     - **Input Validation and Error Raising:** Implement robust input validation and error handling within class methods.

3. **`app/calculation/__init__.py`**
   - **Purpose:** Defines the `Calculation` abstract base class, concrete calculation classes (`AddCalculation`, `SubtractCalculation`, `MultiplyCalculation`, `DivideCalculation`), and the `CalculationFactory` for creating calculation instances.
   - **Key Concepts:**
     - **Inheritance and Polymorphism:** Create a hierarchy of calculation classes that inherit from an abstract base class.
     - **Factory Design Pattern:** Implement a factory to manage the creation of calculation instances.
     - **String Representations:** Define `__str__` and `__repr__` methods for meaningful string representations of objects.

4. **`tests/test_calculations.py`**
   - **Purpose:** Provides unit tests for the calculation classes and the `CalculationFactory`.
   - **Key Concepts:**
     - **Parameterized Testing:** Use `pytest` to run the same test logic with different input values, enhancing test coverage.
     - **Mocking:** Utilize `unittest.mock` to simulate and test interactions between classes.
     - **Exception Handling:** Test that methods correctly raise and handle exceptions.

5. **`tests/test_calculator.py`**
   - **Purpose:** Contains unit tests for the calculator REPL application.
   - **Key Concepts:**
     - **Simulating User Input:** Use `monkeypatch` to simulate user interactions within the REPL.
     - **Capturing Output:** Verify that the correct outputs are displayed based on user inputs.
     - **Negative Testing:** Ensure that the application gracefully handles invalid inputs and unexpected errors.

6. **`tests/test_operations.py`**
   - **Purpose:** Includes unit and negative tests for the `Operation` class's arithmetic methods.
   - **Key Concepts:**
     - **Edge Case Testing:** Test arithmetic methods with various input scenarios, including zero and negative numbers.
     - **Type Validation:** Ensure that methods handle invalid input types appropriately by raising exceptions.

**Supplementary Articles:**
To enhance your understanding of the codebase, please read the following articles:
1. **[Advanced Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)**
2. **[Understanding Design Patterns: Factory Pattern](https://refactoring.guru/design-patterns/factory-method)**
3. **[Mastering Error Handling in Python](https://realpython.com/python-exceptions/)**
4. **[Comprehensive Guide to Testing in Python with pytest](https://realpython.com/pytest-python-testing/)**
6. **[LBYL vs EAFP: Python's Error Handling Paradigms](https://realpython.com/python-lbyl-vs-eafp/)**
7. **[Achieving 100% Test Coverage in Python - Reference Manual on Coverage](https://pytest-cov.readthedocs.io/en/latest/)**


### Watch

Engage with the following instructional videos to reinforce the concepts covered in the codebase and readings:
1. **Video: "Advanced OOP in Python" (20 minutes)**
   - **Purpose:** Dive deeper into OOP concepts such as inheritance, polymorphism, and the factory design pattern.
2. **Video: "Comprehensive Testing with pytest" (20 minutes)**
   - **Purpose:** Learn how to write effective unit and parameterized tests using `pytest`, achieving high test coverage.
3. **Video: "Implementing the Factory Pattern in Python" (15 minutes)**
   - **Purpose:** Understand and implement the factory design pattern to manage object creation.
4. **Video: "Error Handling Best Practices in Python" (15 minutes)**
   - **Purpose:** Explore advanced error handling techniques to create resilient Python applications.
5. **Video: "Achieving 100% Test Coverage in Python" (15 minutes)**
   - **Purpose:** Learn how to measure and attain complete test coverage for your Python projects.

### Review

Utilize the following cheat sheets as quick references to aid your study and project development:
1. **[Advanced OOP Cheat Sheet](https://realpython.com/python-cheat-sheet/)**
   - **Purpose:** Offers a quick reference for advanced OOP concepts and syntax in Python.
2. **[pytest Cheat Sheet](https://realpython.com/python-pytest/)**
   - **Purpose:** Provides essential commands and configurations for writing and running tests with `pytest`.
3. **[Factory Design Pattern Cheat Sheet](https://refactoring.guru/design-patterns/factory-method/python/example)**
   - **Purpose:** Quick reference for implementing the factory design pattern in Python.
4. **[Error Handling Cheat Sheet](https://www.pythonsheets.com/notes/python-exceptions.html)**
   - **Purpose:** Comprehensive guide to Python's error handling mechanisms.
5. **[Test Coverage Cheat Sheet](https://pytest-cov.readthedocs.io/en/latest/)**
   - **Purpose:** Quick reference for measuring and managing test coverage in Python projects.

### Submit

**Activity Type:** Advanced Hands-on Assignment  

**Activity Title:** Professional Calculator Command-Line Application with 100% Test Coverage  

**Grading Type:** Points  

**Submission Instructions:** Submit a link to your GitHub repository containing the project.

**Instructions:** 
- **Repository Setup:**
  - Initialize a new Git repository locally and create a corresponding repository on GitHub.
  - Set up a Python project in your preferred IDE with a well-structured directory layout, following the provided folder structure (`app/calculator/__init__.py`, `app/calculation/__init__.py`, `app/operation/__init__.py`, and `tests/` directory).
  - Create and activate a virtual environment for your project.
  
- **Application Development:**
  - Develop a professional-grade calculator command-line application with the following features:
    - **REPL Interface:** Implement a Read-Eval-Print Loop for continuous user interaction.
    - **Arithmetic Operations:** Allow users to perform addition, subtraction, multiplication, and division.
    - **User Prompts:**
      - Prompt for the desired operation and the numbers to operate on.
      - Provide clear instructions and feedback to the user.
    - **Input Validation:** Validate user inputs to ensure they follow the expected format and handle invalid inputs gracefully.
    - **Error Handling:** 
      - Implement comprehensive error handling to manage invalid inputs and exceptional scenarios (e.g., division by zero).
      - Demonstrate both LBYL (Look Before You Leap) and EAFP (Easier to Ask Forgiveness than Permission) paradigms within your error handling strategies.
    - **Calculation Management:** 
      - Use the `CalculationFactory` to create calculation instances based on user input.
      - Maintain a history of calculations performed during the session.
      - Implement special commands (`help`, `history`, `exit`) to enhance user experience.

- **Best Practices:**
  - **DRY Principle:** Apply the DRY (Don't Repeat Yourself) principle and other best practices to ensure your code is maintainable and efficient.
  - **Modular Design:** Organize your code into modules and classes to enhance readability and reusability.
  
- **Testing:**
  - **Unit Tests:** 
    - Write comprehensive unit tests using `pytest` to verify the functionality of individual components (e.g., arithmetic operations, calculation classes).
    - Ensure that each method and function behaves as expected under various scenarios.
  - **Parameterized Tests:** 
    - Implement parameterized tests in `tests/test_calculations.py` and `tests/test_operations.py` to cover multiple input scenarios efficiently.
    - Achieve extensive test coverage by testing both positive and negative cases.
  - **Test Coverage:** 
    - Use coverage tools (e.g., `pytest-cov`) to measure your test coverage.
    - **Achieve 100% test coverage**, ensuring that all lines of code, branches, and edge cases are tested.
    - **Handling Coverage Exceptions:** 
      - Some lines of code, such as those containing `pass` or `continue`, may not be covered by tests. Research how to use coverage comments (e.g., `# pragma: no cover`) to intentionally ignore these lines without affecting overall coverage metrics.
  
- **Documentation:**
  - Create detailed documentation, including a `README.md` file with setup and usage instructions.
  - Document your code with meaningful comments and docstrings to enhance readability and maintainability.
  
- **Version Control & CI:**
  - **Push Code to GitHub:**
    - Ensure your code follows best practices for code organization and documentation.
    - Commit changes with clear and descriptive messages.
  - **Configure GitHub Actions:**
    - Set up GitHub Actions to automatically run your tests and measure test coverage on each push to the repository.
    - **Enforce 100% Test Coverage:** 
      - Configure your CI pipeline to check for 100% test coverage. If the coverage is below 100%, the build should fail, prompting you to add the necessary tests.
      - Example GitHub Actions workflow file (`.github/workflows/python-app.yml`):
        ```yaml
        name: Python application

        on:
          push:
            branches: [ main ]
          pull_request:
            branches: [ main ]

        jobs:
          build:

            runs-on: ubuntu-latest

            steps:
            - uses: actions/checkout@v2
            - name: Set up Python 3.x
              uses: actions/setup-python@v2
              with:
                python-version: '3.x'
            - name: Install dependencies
              run: |
                python -m pip install --upgrade pip
                pip install pytest pytest-cov
            - name: Run tests with coverage
              run: |
                pytest --cov=app tests/
            - name: Check coverage
              run: |
                coverage report --fail-under=100
        ```
      - **Handling Coverage Exceptions:** 
        - In your code, add comments like `# pragma: no cover` to lines that are intentionally excluded from coverage metrics (e.g., lines with `pass` or `continue`). This ensures that your coverage report accurately reflects the test coverage without being penalized for these lines.
        - Example:
          ```python
          if some_condition:
              pass  # pragma: no cover
          ```

**Grading Expectations:** 
- **Functionality:** Completeness and accuracy of the calculator command-line application, including all specified features.
- **User Interface:** Proper implementation of the REPL pattern and a user-friendly interface that handles user inputs gracefully.
- **Code Quality:** Efficient use of Python control structures, adherence to the DRY principle, and professional coding practices.
- **Error Handling:** Comprehensive error handling mechanisms that manage invalid inputs and exceptional scenarios effectively.
- **Testing:** 
  - Thorough unit and parameterized testing using `pytest`.
  - Achieving **100% test coverage**, ensuring all code paths are tested.
- **Documentation:** Well-structured code with comprehensive documentation, including a clear and informative `README.md`.
- **Automation:** Successful setup of GitHub Actions to automatically run your tests and enforce 100% test coverage, ensuring code quality on every commit.

**Alignment:** 
- Implement advanced Python control structures and OOP principles effectively in a command-line application.
- Apply the DRY principle and other best practices for writing maintainable and efficient Python code.
- Develop a command-line application using the REPL pattern with robust error handling.
- Implement comprehensive unit and parameterized tests for Python applications using `pytest`.
- Achieve and enforce **100% test coverage** through Continuous Integration with GitHub Actions, including handling coverage exceptions where necessary.

### Reflect

**Title:** Module 4 In-Depth Reflection  
**Grading Type:** Points  
**Instructions:**
- **Reflection Essay:** Compose a comprehensive reflection (300-400 words) on your experience developing the professional calculator command-line application.
  - **Application of Concepts:** Analyze how the advanced OOP principles and comprehensive testing techniques learned in this module can be applied to real-world programming scenarios.
  - **Challenges and Solutions:** Discuss any challenges you encountered during the project, particularly in implementing OOP concepts or achieving full test coverage, and the strategies you used to overcome them.
  - **Self-Evaluation:** Evaluate your current level of confidence in using advanced OOP and testing tools. Identify areas where you feel proficient and areas where you need further practice or support.
- **Purpose:** This activity aims to encourage deep metacognition and help you connect new knowledge with prior experiences and future applications.

### Quiz

**Title:** Advanced Python Programming and Comprehensive Testing Quiz  
**Grading Type:** Points  
**Instructions:**
- **Comprehensive Assessment:** Complete a comprehensive quiz covering the advanced OOP concepts, error handling strategies, and testing methodologies introduced in this module.
  - **Topics Covered:** 
    - Advanced Object-Oriented Programming (inheritance, polymorphism, encapsulation)
    - Factory Design Pattern
    - Error Handling Paradigms (LBYL vs EAFP)
    - Writing Unit and Parameterized Tests with `pytest`
    - Achieving and Enforcing Test Coverage
    - Handling Coverage Exceptions
  - **Question Types:** The quiz will include multiple-choice, short answer, and code analysis questions to thoroughly evaluate your comprehension and application of the module's content.
- **Preparation:** 
  - Review all provided materials, including the codebase, supplementary articles, instructional videos, and cheat sheets.
  - Ensure you understand how to implement and test advanced OOP concepts.
  - Familiarize yourself with using coverage tools and handling coverage exceptions in `pytest`.

---

This updated module leverages the provided codebase as your primary textbook, allowing you to learn by doing. By engaging with the well-commented code, completing hands-on assignments with stringent testing requirements, and reflecting on your learning process, you will build a strong foundation in advanced Object-Oriented Programming and comprehensive testing in Python. Embrace the opportunity to write clean, efficient, and thoroughly tested code, ensuring high-quality applications through **100% test coverage** and optimized testing strategies.
