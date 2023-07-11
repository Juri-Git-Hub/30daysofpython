from random import shuffle

ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")

cards = [(rank, suit) for suit in suits for rank in ranks]

def shuffle_deck(cards):
    deck = list(cards)
    shuffle(deck)

    return iter(deck)


def get_players():
    while True:
        number_of_players = input("How many players are there?")

        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("That wasn't a number!")
        else:
            if number_of_players in range(2,11):
                return number_of_players
            else:
                if number_of_players < 2:
                    print("There must be atleast 2 players!")
                else:
                    print("You can have a maximum of 10 players!")
    

def deal(cards, number_of_players):
    deck = shuffle_deck(cards)
    
    deal_players(deck, number_of_players)

    deal_table(deck)


def deal_players(deck, number_of_players):
    first_cards = [next(deck) for _ in range(number_of_players)]
    second_cards = [next(deck) for _ in range(number_of_players)]
    
    player_hands = zip(first_cards, second_cards)
    
    for i, (first_card, second_card) in enumerate(player_hands, start=1):
        print(f"Player {i} was dealt: {first_card}, {second_card}")


def deal_table(deck):
    burn = next(deck)
    flop = []
    flop.append(next(deck))
    flop.append(next(deck))
    flop.append(next(deck))
    print(f"The flop: {flop}")
    burn = next(deck)
    turn = next(deck)
    print(f"The turn: {turn}")
    burn = next(deck)
    river = next(deck)
    print(f"The river: {river}")
    


deal(cards, get_players())