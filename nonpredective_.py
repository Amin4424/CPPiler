from lexer import lexer
from constants import dic_col , dic_row, grammers , rows , columns
def NonPredctive():
    code = input("Enter your code: \n")
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
            print(a[0])
            a.pop(0)
        elif head not in key_list:
            print("not possible")
            break
        elif rows[m][n] !="":
            stack.pop()
            b = rows[m][n].split()
            for i in b:
                stack.append(i)
            print(b)
        else:
            print("not possible")
            break