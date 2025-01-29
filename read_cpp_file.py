def read_cpp_file(file_path):
    try:
        with open(file_path, 'r') as file:
            cpp_code = file.read()
        return cpp_code
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None
def open_cpp_file(file_path):
    cpp_code_string = read_cpp_file(file_path)
    if cpp_code_string:
        return cpp_code_string