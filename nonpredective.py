from anytree import Node, RenderTree
from anytree.exporter import DotExporter
from rich.console import Console
from rich.table import Table


from lexer import lexer
from constants import dic_col , dic_row, grammers , rows , columns

import read_cpp_file

def NonPredctive():
    file_path = input("Enter the file path: ")
    code = read_cpp_file.open_cpp_file(file_path)
    tokens = lexer(code)
    a = []
    key_list = grammers.keys()
    for token in tokens:
        a.append(token[1])
    stack = ['$', 'Start']
    head = stack.pop()
    while head!='$':
        n = dic_col[a[0]]
        m = dic_row[head]
        if head == a[0]:
            a.pop(0)
        elif head not in key_list:
            print("not possible")
            break
        elif rows[m][n] !="":
            stack.pop()
            b = rows[m][n].split()
            for i in b:
                stack.append(i)
            break
        else:
            print("not possible")
            break
    root = Node("Parse Tree")
    for row in rows:
        parent_node = Node(row[0], parent=root)
        for i in range(1, len(row)):
            if row[i]:
                Node(f"{columns[i]}: {row[i]}", parent=parent_node)
    for pre, fill ,node in RenderTree(root):
        print("%s%s" % (pre, node.name))

"""
O(n) for reading the file and tokenizing the code.
O(t) for processing tokens.
O(t) for parsing with the stack.
O(r * c) for building the parse tree.
O(n) for rendering the parse tree.
overall :  O(n + t + r * c)
"""