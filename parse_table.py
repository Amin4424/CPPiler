from rich.console import Console
from rich.table import Table
from constants import rows , columns

def Print_Parse_Table():
    console = Console()
    table = Table(title="Parse Table")
    for column in columns:
        table.add_column(column, style="magenta")
    for row in rows:
        table.add_row(*row)
    console.print(table)

"""
O(n)
"""