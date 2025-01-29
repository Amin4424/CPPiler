import lexer
from rich.console import Console
from rich.table import Table
from hashlib import sha256
def Print_Table():
    print("Input the code")
    code = input()
    console = Console()
    tokens = lexer.lexer(code)
    table = Table(title="Token Table")
    table.add_column("string", justify="center", style="cyan", no_wrap=True)
    table.add_column("number", justify="center", style="cyan", no_wrap=True)
    table.add_column("symbol", justify="center", style="cyan", no_wrap=True)
    table.add_column("identifier", justify="center", style="cyan", no_wrap=True)
    table.add_column("reservedword", justify="center", style="cyan", no_wrap=True)

    string = []
    number = []
    symbol = []
    identifier = []
    reservedword = []

    tokens.sort(key=lambda x: x[1])

    for token in tokens:
        if token[0] == "string":
            string.append(sha256(token[1].encode()).hexdigest())
        elif token[0] == "number":
            number.append(sha256(token[1].encode()).hexdigest())
        elif token[0] == "symbol":
            symbol.append(sha256(token[1].encode()).hexdigest())
        elif token[0] == "identifier":
            identifier.append(sha256(token[1].encode()).hexdigest())
        elif token[0] == "reservedword":
            reservedword.append(sha256(token[1].encode()).hexdigest())

    table = Table(title="Token Table")
    table.add_column("STRING", style="cyan")
    table.add_column("NUMBER", style="yellow")
    table.add_column("SYMBOL", style="green")
    table.add_column("IDENTIFIER", style="blue")
    table.add_column("RESERVEDWORD", style="red")

    max_length = max(len(string), len(number), len(symbol), len(identifier), len(reservedword))

    for i in range(max_length):
        table.add_row(
            string[i] if i < len(string) else "",
            number[i] if i < len(number) else "",
            symbol[i] if i < len(symbol) else "",
            identifier[i] if i < len(identifier) else "",
            reservedword[i] if i < len(reservedword) else "",
        )

    console.print(table)
