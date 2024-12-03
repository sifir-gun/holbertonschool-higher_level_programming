# Python - Everything is Object

## Background Context

In Python, **everything is an object**. This project dives deep into understanding how Python works with objects, variables, and references, and how these concepts affect mutable and immutable types.

Have you ever encountered unexpected results when working with variables? For example:

```python
a = 1
b = a
a = 2
print(b)  # Output: 1
```

Or this?

```python
l = [1, 2, 3]
m = l
l[0] = 'x'
print(m)  # Output: ['x', 2, 3]
```

Understanding these behaviors is critical for writing clean, predictable Python code. This project is designed to challenge you to think, brainstorm, and internalize the concepts behind such examples **before testing them in code**.

## Learning Objectives

By the end of this project, you will be able to:

* Define what an **object** is in Python
* Differentiate between a **class** and an **instance**
* Explain **mutable** vs **immutable** objects
* Understand **references**, **assignments**, and **aliases**
* Identify when two variables point to the same object
* Use Python functions to inspect objects (e.g., id and type)
* Recognize built-in **mutable** and **immutable** types
* Understand how Python passes variables to functions

## Resources

To prepare for this project, review the following resources:

* 9.10. Objects and values
* 9.11. Aliasing
* Immutable vs Mutable Types
* Cloning Lists
* Python Tuples: Immutable but Potentially Changing

## Requirements

### Python Scripts

* **Editor:** Use vi, vim, or emacs
* **Execution:** All scripts will be interpreted with Python 3.8.5 on Ubuntu 20.04 LTS
* **Formatting:** Follow pycodestyle (v2.7.*) standards
* **Shebang:** Include #!/usr/bin/python3 on the first line of all Python files
* **Executability:** All Python files must be executable

### Answer Files (.txt)

* **Format:** One-line answers without spaces before or after the answer
* **Content:** No shebang (#!/usr/bin/python3) required
* **Newline:** Each file must end with a new line

### Directory Structure

```
holbertonschool-higher_level_programming/
└── python-everything_is_object/
    ├── 0-answer.txt
    ├── 1-answer.txt
    ├── 2-answer.txt
    ├── 3-answer.txt
    ├── ...
    ├── 19-copy_list.py
    ├── 29-blog_post.md
    └── README.md
```