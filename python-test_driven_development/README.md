# Python Test Driven Development (TDD)

## Background Context

**Important notice on intranet checks for Python projects**

Starting from today:
- Based on the requirements of each task, you should always write the documentation (module(s) + function(s)) and tests first, before you actually code anything.
- The intranet checks for Python projects won’t be released before their first deadline, in order for you to focus more on TDD and think about all possible cases.
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case. But not in the implementation of them!
- Don’t trust the user, always think about all possible edge cases.

## Resources
- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://docs.python.org/3.8/library/doctest.html)
- [Unit Tests in Python](https://docs.python.org/3/library/unittest.html)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

### General:
- Why Python programming is awesome
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- All your test files should be text files (extension: `.txt`)
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have documentation (e.g., `python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have documentation (e.g., `python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining the purpose of the module, class, or method. The length of it will be verified.
- The checker is checking for tests!

## Tasks

### 0. Integers addition
Write a function that adds 2 integers.
- Prototype: `def add_integer(a, b=98):`
- `a` and `b` must be integers or floats, otherwise raise a `TypeError` exception.
- You are not allowed to import any module.

### 1. Divide a matrix
Write a function that divides all elements of a matrix.
- Prototype: `def matrix_divided(matrix, div):`
- You are not allowed to import any module.

### 2. Say my name
Write a function that prints `My name is <first name> <last name>`.
- Prototype: `def say_my_name(first_name, last_name=""):`
- You are not allowed to import any module.

### 3. Print square
Write a function that prints a square with the character `#`.
- Prototype: `def print_square(size):`
- You are not allowed to import any module.

### 4. Text indentation
Write a function that prints a text with 2 new lines after each of these characters: `.`, `?`, and `:`.
- Prototype: `def text_indentation(text):`
- You are not allowed to import any module.

### 5. Max integer - Unittest
Write unittests for the function `def max_integer(list=[]):`.
- Your test file should be inside a folder `tests`.
- You have to use the `unittest` module.

## Repository
- **GitHub repository**: `holbertonschool-higher_level_programming`
- **Directory**: `python-test_driven_development`
