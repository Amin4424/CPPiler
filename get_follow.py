from lexer import lexer
from constants import grammers
from get_first import First ,holder_first

holder_follow = []
visited = set()
key_list = grammers.keys()

def Follow(grammer):
    global holder_follow
    global holder_first
    if grammer in visited:
        return
    visited.add(grammer)
    if grammer == 'Start':
        holder_follow.append('$')
        return
    for non_terminal, productions in grammers.items():
        for production in productions:
            items = production.split()
            if grammer in items:
                tokens = lexer(production)
                right_hand = []
                if tokens:
                    for token in tokens:
                        right_hand.append(token[1])
                    right_hand.append('ϵ')
                for i in range(len(right_hand)):
                    if grammer == right_hand[i]:
                        if i + 1 < len(right_hand):
                            if right_hand[i + 1] != 'ϵ':
                                if right_hand[i + 1] in key_list:
                                    holder_first = []
                                    holder_follow.extend(First(right_hand[i + 1]))
                                    if 'ϵ' in First(right_hand[i + 1]):
                                        Follow(non_terminal)
                                else:
                                    if right_hand[i + 1] in ['}',')']:
                                        if right_hand[i - 1] in ['{', '(']:
                                            holder_follow.append(right_hand[i + 1])
                                    else:
                                        holder_follow.append(right_hand[i + 1])
                            else:
                                Follow(non_terminal)
                        else:
                            Follow(non_terminal)
    final_holder = []
    for item in holder_follow:
        if item not in final_holder and item !='ϵ':
            final_holder.append(item)
    return final_holder
