from rich.console import Console
from rich.table import Table

import os
import token_table
import parse_table
import tokenize_code
console = Console()

def show_menu():
    table = Table(title="Main Menu")

    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", justify="center", style="magenta")

    table.add_row("1", "Tokenize")
    table.add_row("2", "Token Table")
    table.add_row("3", "Parse Table")
    table.add_row("4", "Exit")

    console.print(table)

def main():
    os.system("cls")
    show_menu()
    option = input("Please select an option: ")
    ProgramContinue = True
    while ProgramContinue:
        os.system("cls")
        if option == "1":
            tokenize_code.Tokenize()
        elif option == "2":
            token_table.Print_Table()
        elif option == "3":
            parse_table.Print_Parse_Table()

        elif option == "4":
            ProgramContinue = False
            break
        else:
            console.print("Invalid option", style="bold red")
        show_menu()
        option = input("Please select an option: ")
    

if __name__ == "__main__":
    main()
