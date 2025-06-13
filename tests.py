from functions.get_files_info import get_files_info, get_file_content

test1 = get_file_content("calculator", "main.py")
print(test1)

test2 = get_file_content("calculator", "pkg/calculator.py")
print(test2)

test3 = get_file_content("calculator", "/bin/cat")
print(test3)
