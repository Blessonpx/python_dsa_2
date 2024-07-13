import importlib.util
import sys

def import_and_run_module(module_name):
    spec = importlib.util.spec_from_file_location(module_name, module_name)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)

if __name__ == "__main__":
    print("DSA Problem Sets")
    print("Enter File_name to run")
    filename = input("Enter the filename (with .py extension): ")
    try:
        import_and_run_module(filename)
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
