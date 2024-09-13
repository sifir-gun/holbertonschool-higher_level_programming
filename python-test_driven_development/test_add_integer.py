import importlib.util
import sys

# Chemin vers le fichier 0-add_integer.py
module_name = "add_integer"
file_path = "./0-add_integer.py"

# Charger le module dynamiquement
spec = importlib.util.spec_from_file_location(module_name, file_path)
module = importlib.util.module_from_spec(spec)
sys.modules[module_name] = module
if spec is not None:
    module = importlib.util.module_from_spec(spec)
    module.__loader__.exec_module(module)
else:
    raise ImportError("Failed to load module")

# Importer la fonction add_integer du module chargé
add_integer = module.add_integer

# Exécuter les doctests
if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/0-add_integer.txt")