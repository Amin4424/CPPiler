import lexer
from rich.console import Console

import read_cpp_file

def Tokenize():
    file_path = input("Enter the file path: ")
    code = read_cpp_file.open_cpp_file(file_path)
    console = Console()
    tokens = lexer.lexer(code)
    lines = []
    lines = code.split('\n')
    counter = 0 
    for line in lines:
        counter += 1
        if not(line[-1] == ";" or line[-1] == "}" or line[-1] == "{" or line[-1] == ")" or line[0] == "#"):
            console.print(f"[bold red]Missing semicolon at {counter}[/bold red]")
    counter = 0
    for line in lines:
        counter += 1
        if "int" in line:
            line_token = lexer.lexer(line)
            for token in line_token:
                if token[0] == "string":
                    console.print(f"[bold red]Invalid type at {counter}[/bold red]")
    for token in tokens:
        console.print(token)