# _*_ coding: utf-8 _*_


def sort_cards(cards):

    for n, i in enumerate(cards):
        if i == 'A':
            cards[n] = '0'
        if i == 'T':
            cards[n] = '10'
        if i == 'J':
            cards[n] = '11'
        if i == 'Q':
            cards[n] = '12'
        if i == 'K':
            cards[n] = '13'

    cards.sort(key=int)

    for n, i in enumerate(cards):
        if i == '0':
            cards[n] = 'A'
        if i == '10':
            cards[n] = 'T'
        if i == '11':
            cards[n] = 'J'
        if i == '12':
            cards[n] = 'Q'
        if i == '13':
            cards[n] = 'K'

    return cards
