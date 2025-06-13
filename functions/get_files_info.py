import os

def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    dir_path = os.path.abspath(os.path.join(working_dir_path, directory or "."))
    if not dir_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        directory_contents = os.listdir(dir_path)
        meta_contents = []
        for i in directory_contents:
            filesize = os.path.getsize(os.path.join(dir_path, i))
            is_dir = os.path.isdir(os.path.join(dir_path, i))
            meta_contents.append(f'- {i}: file_size={filesize}, is_dir={is_dir}')
        return "\n".join(meta_contents)
    except Exception as e:
        return f"Error listing files: {e}"


def get_file_content(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    full_file_path = os.path.abspath(os.path.join(working_dir_path, file_path))
    if not full_file_path.startswith(working_dir_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(full_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        MAX_CHARS = 10000
        print(full_file_path)
        with open(full_file_path, "r") as f:
            file_contents_string = f.read(MAX_CHARS)
            if len(f.read(1)) > 0:
                file_contents_string = file_contents_string + f'[...File "{file_path}" truncated at 10000 characters]'
        return file_contents_string
    except Exception as e:
        return f"Error reading file: {e}"
        
