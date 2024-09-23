# Python Inheritance Project

## Resources
Read or watch:
- [Inheritance](https://docs.python.org/3/tutorial/classes.html#inheritance)
- [Multiple inheritance](https://en.wikipedia.org/wiki/Multiple_inheritance)
- [Inheritance in Python](https://realpython.com/python-inheritance/)
- [Learn to Program 10: Inheritance Magic Methods](https://www.youtube.com/watch?v=ik0Uhl6R5JQ)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is a superclass, baseclass, or parentclass
- What is a subclass
- How to list all attributes and methods of a class or instance
- When can an instance have new attributes
- How to inherit a class from another
- How to define a class with multiple base classes
- What is the default class every class inherits from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by inheritance to subclasses
- What is the purpose of inheritance
- What are, when, and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
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
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### Documentation
- Do not use the words `import` or `from` inside your comments, the checker will think you are trying to import some modules.

## Quiz Questions
- Great! You've completed the quiz successfully! Keep going!

## Tasks

### 0. Lookup
Write a function that returns the list of available attributes and methods of an object:

Prototype: `def lookup(obj):`

- Returns a list object
- You are not allowed to import any module

**Example:**
```bash
$ ./0-main.py
['__class__', '__delattr__', '__dict__', ...]
