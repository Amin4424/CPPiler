import re
from hashlib import sha256


def lexer(code):
    TOKENS = [
    ('reservedword', r'int|float|void|return|if|while|cin|cout|continue|break|#include|using|iostream|namespace|std|main'),
    ('identifier', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('number', r'[0-9]+(\.[0-9]+)?'), 
    ('symbol', r'>=|<=|==|!=|\|\||<<|>>|\+|\-|\*|/|=|;|,|{|}|\(|\)|>|<'),
    ('whitespace', r'\s+'),
    ('string', r'"[^"]*"'),
]

    TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS)
    tokens = [] 
    for match in re.finditer(TOKEN_REGEX, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'whitespace':
            tokens.append((token_type, token_value))
    
    return tokens


def create_token_table(tokens):
    
    token_table_names = {
        'string': [],
        'number': [],
        'symbol': [],
        'identifier': [],
        'reservedword': [],
    }

    for token_type, token_value in tokens:
        token_table_names[token_type].append((token_value, sha256(token_value.encode()).hexdigest()))

    for token_name in token_table_names:
        token_table_names[token_name].sort(key=lambda x: x[0])

    token_table = []
    for token_name in ['string', 'number', 'symbol', 'identifier', 'reservedword']:
        token_table.extend(token_table_names[token_name])

    return token_table

grammar = {
    'Start': ['SNM'],
    'S': ['#include S', 'ϵ'],
    'N': ['using namespace std;', 'ϵ'],
    'M': ['int main(){T V}'],
    'T': ['Id T', 'L T', 'Loop T', 'Input T', 'Output T', 'ϵ'],
    'V': ['return 0;', 'ϵ'],
    'Id': ['int L', 'float L'],
    'L': ['identifier Assign Z'],
    'Z': [', identifier Assign Z', ';'],
    'Operation': ['number P', 'identifier P'],
    'P': ['OW P', 'ϵ'],
    'O': ['+', '-', '*'],
    'W': ['number', 'identifier'],
    'Assign': ['= Operation', 'ϵ'],
    'Expression': ['Operation K Operation'],
    'K': ['==', '>=', '<=', '!='],
    'Loop': ['while(Expression){T}'],
    'Input': ['cin >> identifier F;'],
    'F': ['>> identifier F', 'ϵ'],
    'Output': ['cout << CH;'],
    'H': ['<< CH', 'ϵ'],
    'C': ['number', 'string', 'identifier'],
}

# def get_first(grammer):
    

code = '''
#include <iostream>
using namespace std;
int main(){
int x;
int s=0, t=10;
while (t >= 0){
cin>>x;
t = t - 1;
s = s + x;
}
cout<<"sum="<<s;
return 0;
}
'''
tokens = lexer(code)


output = []
for token in tokens:
    output.append(f"[{token[0]}, {token[1]}]")
for item in output:
    print(item)