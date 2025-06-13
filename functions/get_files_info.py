import os

def get_files_info(working_directory, directory=None):
    working_dir_path = os.path.abspath(working_directory)
    dir_path = os.path.abspath(os.path.join(working_dir_path, directory or "."))
    if not dir_path.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    directory_contents = os.listdir(dir_path)
    meta_contents = []
    for i in directory_contents:
        try:
            filesize = os.path.getsize(os.path.join(dir_path, i))
            is_dir = os.path.isdir(os.path.join(dir_path, i))
            meta_contents.append(f'- {i}: file_size={filesize}, is_dir={is_dir}')
        except Exception as e:
            meta_contents.append(f"Error: {e}")
    return "\n".join(meta_contents)
