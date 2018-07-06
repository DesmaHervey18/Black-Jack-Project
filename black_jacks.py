from random import shuffle


def hand_score(hand):
    ''' list[card] -> int

    >>> hand_score([2,3,4])
    9
    >>> hand_score([7, 'Q'])
    17
    >>> hand_score(['A', 5])
    16
    '''
    total = 0
    for card in hand:
        total += value_of_cards(card)
    return total


def value_of_cards(card):
    ''' str -> number
    Return the value of the card.
    >>> value_of_card ('K').
    10
    '''

    if card == 'K':
        return 10
    if card == 'Q':
        return 10
    if card == 'J':
        return 10
    if card == 'A':
        return 11
    else:
        return card


def black_jack():
    deck = [
        2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7,
        8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 11, 11, 11, 11, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10
    ]
    shuffle(deck)
    player = deck[:2]
    dealer = deck[2:4]
    while True:
        print(player)
        print(sum(player))
        response = input('Player: Do you want to hit or stay?')
        if response == 'hit':
            player.append(deck.pop())
        if hand_score(player) > 21:
            print('Player: BUSTED')
            #     total = sum(dealer_name)
            #     while total < 17

            print('Dealer: WINNER')
            break
        if hand_score(player) == 21:
            print('Player: BLACK JACK')
            #     total = sum(dealer_name)
            #     while total < 17

            break
        if response == 'stay':
            break

    while True:
        print(dealer)
        print(sum(dealer))
        response = input('Dealer: Do you want to hit or stay?')
        if response == 'hit':
            dealer.append(deck.pop())
        if hand_score(dealer) > 21:
            print('Dealer: BUSTED')
            print('Player: WINNER')
            break
        elif hand_score(dealer) == 21:
            print('Dealer: BLACK JACK')
            break
        elif response == 'stay':
            if dealer > player:
                return True
            break
    hand_score(dealer)
    hand_score(player)


# def dealer_call(dealer_name, deck):
#     total = sum(dealer_name)
#     while total < 17a


def main():
    black_jack()
    # if player_deck == 21 dealer_deck:


if __name__ == '__main__':
    main()
