import random

class Card:
    def __init__(self, value, shape):
        self.value = value
        self.shape = shape

class Deck: 
    def __init__(self):
        arr_val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        arr_shape = ["Spade", "Heart", "Club", "Diamond"]

        #list to hold the cards of the deck
        self.arr_deck = []

        for shape in arr_shape:
            for val in arr_val:
                c = Card( val, shape )
                self.arr_deck.append(c)

    #Method to shuffle deck
    def shuffle(self):
        for i in range (52):

            #Get a random index
            rand_idx = random.randrange(0, 52, 1)

            #save the card at that random index
            temp_card = self.arr_deck[rand_idx]

            #Swap the places of the two cards
            self.arr_deck[rand_idx] = self.arr_deck[i]
            self.arr_deck[i] = temp_card

    #Method to draw a card
    def draw(self):
        return self.arr_deck.pop()
    
    #Method to reset the deck
    def reset_deck(self):
        self.__init__()


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []


class Blackjack:
    def __init__(self):
        self.dealer = Player("dealer")
        self.player = Player("player")

        self.jack_deck = Deck()
        self.jack_deck.shuffle()

    def setup_dealer(self):
        self.dealer.hand.append(self.jack_deck.pop())
        self.dealer.hand.append(self.jack_deck.pop())
        self.dealer.hand.append(self.jack_deck.pop())
        print(self.dealer.hand[0], self.dealer.hand[1])

            
    def sum_hand(self, player):
        sum = 0
        ace_count = 0
        for card in player.hand:
            temp_val = card_value(card)
            if temp_val is "A":
                ace_count += 1
            else:
                sum += temp_val

        while ace_count > 0:
            if sum + 11 <= 21:
                sum += 11
            else:
                sum += 1
            ace_count -= 1
        

    def card_value(self, card):
        value = -1
        if card[0] == "J" or card[0] == "Q" or card[0] == "K":
            value = 10
        elif card[0] == "A":
            value = "A"
        else:
            value = card[0]

        return value

    def hit(self):
        player.hand.append(jack_deck.draw())

