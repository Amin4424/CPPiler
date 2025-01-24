from hashlib import sha256
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
