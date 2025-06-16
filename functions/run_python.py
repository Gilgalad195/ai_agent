import os
import subprocess

def run_python_file(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(working_dir_path, file_path))
    if not full_file_path.startswith(working_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(full_file_path):
        return f'Error: File "{file_path}" not found.'
    if not full_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    process_object = subprocess.run(["python3", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=working_dir_path, timeout=30)
        

        