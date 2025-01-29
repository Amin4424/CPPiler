from lexer import lexer
from constants import grammers
holder_first = []
def First(grammer):
    global holder_first
    for production in grammers[grammer]:
        tokens = lexer(production)
        if tokens:
            right_hand = tokens[0][1]
            if right_hand in grammers:
                First(right_hand)
            else:
                holder_first.append(right_hand)
        else:
            holder_first.append(production)
    return holder_first
"""
O(N * M * L)
"""