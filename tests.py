from functions.get_files_info import get_files_info, get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

test1 = run_python_file("calculator", "main.py")
print(test1)

test2 = run_python_file("calculator", "tests.py")
print(test2)

test3 = run_python_file("calculator", "../main.py")
print(test3)

test4 = run_python_file("calculator", "nonexistent.py")
print(test4)
