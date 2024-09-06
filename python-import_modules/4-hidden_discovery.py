#!/usr/bin/python3
import sys
import os

# Add the directory containing 'hidden_4' to the Python module search path
module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
