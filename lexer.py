import re
TOKENS = [
    ('reservedword', r'int|float|void|return|if|while|cin|cout|continue|break|#include|using|iostream|namespace|std|main'),
    ('identifier', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('number', r'[0-9]+(\.[0-9]+)?'), 
    ('symbol', r'>=|<=|==|!=|\|\||<<|>>|\+|\-|\*|/|=|;|,|{|}|\(|\)|>|<'),
    ('whitespace', r'\s+'),
    ('string', r'"[^"]*"'),
]

def lexer(code):
    TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKENS)
    tokens = [] 
    for match in re.finditer(TOKEN_REGEX, code):
        token_type = match.lastgroup
        token_value = match.group(token_type)
        if token_type != 'whitespace':
            tokens.append((token_type, token_value))
    return tokens
"""
O(m * n)
"""
