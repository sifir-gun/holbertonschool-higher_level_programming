# Python - More Data Structures: Set, Dictionary

## Resources
Read or watch:
- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://book.pythontips.com/en/latest/map_filter.html)
- [Learn to Program 12 Lambda Map Filter Reduce](https://youtu.be/1GAC6KQUPeg)

man or help:
- `python3`

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- Why Python programming is awesome
- What are sets and how to use them
- What are the most common methods of set and how to use them
- When to use sets versus lists
- How to iterate into a set
- What are dictionaries and how to use them
- When to use dictionaries versus lists or sets
- What is a key in a dictionary
- How to iterate over a dictionary
- What is a lambda function
- What are the map, reduce and filter functions

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle` (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### 0. Squared simple
Write a function that computes the square value of all integers of a matrix.

- Prototype: `def square_matrix_simple(matrix=[]):`
- Matrix is a 2 dimensional array.
- Returns a new matrix:
  - Same size as the matrix
  - Each value should be the square of the value of the input
  - Initial matrix should not be modified
- You are allowed to use regular loops, map, etc.

### 1. Search and replace
Write a function that replaces all occurrences of an element by another in a new list.

- Prototype: `def search_replace(my_list, search, replace):`
- You are not allowed to import any module.

### 2. Unique addition
Write a function that adds all unique integers in a list (only once for each integer).

- Prototype: `def uniq_add(my_list=[]):`
- You are not allowed to import any module.

### 3. Present in both
Write a function that returns a set of common elements in two sets.

- Prototype: `def common_elements(set_1, set_2):`
- You are not allowed to import any module.

### 4. Only differents
Write a function that returns a set of all elements present in only one set.

- Prototype: `def only_diff_elements(set_1, set_2):`
- You are not allowed to import any module.

### 5. Number of keys
Write a function that returns the number of keys in a dictionary.

- Prototype: `def number_keys(a_dictionary):`
- You are not allowed to import any module.

### 6. Print sorted dictionary
Write a function that prints a dictionary by ordered keys.

- Prototype: `def print_sorted_dictionary(a_dictionary):`
- You can assume that all keys are strings.
- You are not allowed to import any module.

### 7. Update dictionary
Write a function that replaces or adds key/value in a dictionary.

- Prototype: `def update_dictionary(a_dictionary, key, value):`
- You are not allowed to import any module.

### 8. Simple delete by key
Write a function that deletes a key in a dictionary.

- Prototype: `def simple_delete(a_dictionary, key=""):`
- You are not allowed to import any module.

### 9. Multiply by 2
Write a function that returns a new dictionary with all values multiplied by 2.

- Prototype: `def multiply_by_2(a_dictionary):`
- You are not allowed to import any module.

### 10. Best score
Write a function that returns a key with the biggest integer value.

- Prototype: `def best_score(a_dictionary):`
- If no score is found, return `None`.
- You are not allowed to import any module.

### 11. Multiply by using map
Write a function that returns a list with all values multiplied by a number without using any loops.

- Prototype: `def multiply_list_map(my_list=[], number=0):`
- You have to use `map`.
- Your file should be max 3 lines.

### 12. Roman to Integer
Create a function that converts a Roman numeral to an integer.

- Prototype: `def roman_to_int(roman_string):`
- You can assume the number will be between 1 to 3999.
- If the `roman_string` is not a string or `None`, return 0.