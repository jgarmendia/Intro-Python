# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
my_hand = []
my_deck = []
dealer_hand = []
busted = False
phase = ""
draw_dealer = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    
    
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand_list = []
                
    def __str__(self):
        #return a string representation of a hand
        ans = ""
        s = "Hand contains "
        for i in range(len(self.hand_list)):
            ans += str(self.hand_list[i]) + " "
        return s + ans
    
    def add_card(self, card):
        # add a card object to a hand
        self.card = card
        self.hand_list.append(self.card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        ace = False
        for c in self.hand_list:
            value += VALUES[c.get_rank()]
            if c.get_rank() == 'A':
                ace = True
        if value + 10 <= 21 and ace == True:
            return value + 10
        else:
            return value   
              

    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for c in self.hand_list:
            c.draw(canvas, pos)
            pos[0] += 100
 
  
        
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck_list = []
        # create a Card object using Card(suit, rank) and add it to the card list for the deck 
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck_list.append(card)
        
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck       
        random.shuffle(self.deck_list)

    def deal_card(self):
        # deal a card object from the deck
        deal = self.deck_list.pop()
        return deal
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        s = "Deck contains "
        for i in range(len(self.deck_list)):
            ans += str(self.deck_list[i]) + " "
        return s + ans


#define event handlers for buttons
def deal():
    global outcome, in_play, my_deck, my_hand, dealer_hand, score, busted, phase, draw_dealer

    # your code goes here
    my_deck = Deck()
    my_deck.shuffle()
    
    my_hand = Hand()
    my_hand.add_card(my_deck.deal_card())
    my_hand.add_card(my_deck.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(my_deck.deal_card())
    dealer_hand.add_card(my_deck.deal_card())
    
    
    busted = False
    outcome = ""
    phase = "Hit or Stand?"
    draw_dealer = True
    
#    print "my hand =" , my_hand
#    print "dealer hand =" , dealer_hand
    
    if in_play == True:
        outcome = "You have busted."
        busted = True
        phase = "Hit or stand?"
        score -= 1
    in_play = True    
    busted = False
    
def hit():
    # replace with your code below
    global in_play, outcome, my_hand, my_deck, score, busted, phase
    if in_play:
        if my_hand.get_value() <= 21:
            my_hand.add_card(my_deck.deal_card())
            if my_hand.get_value() > 21:
                outcome = "You have busted."
#                print outcome
                busted = True
                in_play = False
                score -= 1
                phase = "New deal?"
#    print my_hand
#    print score    
    # if the hand is in play, hit the player
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    # replace with your code below
    global outcome, dealer_hand, my_hand, my_deck, in_play, score, busted, phase
    if busted == True:
        outcome = "You have busted."
#        print outcome
        phase = "New deal?"
        in_play = False
    if in_play == False:
        phase = "New deal?"
        None 
    else:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        if dealer_hand.get_value() > 21 and in_play == True:
            outcome = "Dealer have busted."
            score += 1
#            print outcome
            in_play = False
            phase = "New deal?"
        else:
            if my_hand.get_value() <= dealer_hand.get_value() and in_play == True:
                outcome = "You have busted."
                score -= 1
#                print outcome
                in_play = False
                phase = "New deal?"
            else:
                if in_play == True:
                    outcome = "Dealer have busted."
                    score += 1
#                    print outcome
                    in_play = False
                    phase = "New deal?"
        
#    print "dealer hand =", dealer_hand
#    print score
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
# test to make sure that card.draw works, replace with your code below
#    card = Card("S", "A")
#    card.draw(canvas, [300, 300])
    canvas.draw_text("Blackjack", [230, 80], 40, "Black")
    canvas.draw_text(("Score = " + str(score)), [480, 120], 25, "Red")
    canvas.draw_text(str(outcome), [230, 300], 25, "White")
    canvas.draw_text(str(phase), [230, 330], 25, "Yellow")
    
    if in_play == True:
        pos1 = [10, 400]
        my_hand.draw(canvas, pos1)
        pos2 = [10, 100]
        dealer_hand.draw(canvas, pos2)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [pos2[0] - 91 - CARD_BACK_SIZE[0], pos2[1] + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        if draw_dealer == True:
            pos1 = [10, 400]
            my_hand.draw(canvas, pos1)
            pos2 = [10, 100]
            dealer_hand.draw(canvas, pos2)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# remember to review the gradic rubric