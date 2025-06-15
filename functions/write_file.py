import os

def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(working_dir_path, file_path))
    if not full_file_path.startswith(working_dir_path):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(full_file_path):
            os.makedirs(os.path.dirname(full_file_path))
        with open(full_file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"
    