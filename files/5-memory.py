# implementation of card game - Memory

import simplegui
import random

#Globals

WIDTH = 800
HEIGHT = 100


card_list1 = [0, 1, 2, 3, 4, 5, 6, 7]
card_list2 = [0, 1, 2, 3, 4, 5, 6, 7]
deck = card_list1 + card_list2
exposed = [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
state = 0
moves = 0
card1 = 0
card2 = 0

# helper function to initialize globals
def init():
    global state, moves, exposed
    random.shuffle(deck)  
    state = 0
    moves = 0
    exposed = [ False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False] 
    card1 = 0
    card2 = 0
    label.set_text("Moves = "+str(moves))
    
# define event handlers
def mouseclick(pos):
    global exposed, state, card1, card2, moves, deck
    card = pos[0] // 50
    print "card num", card
    if not exposed[card]:
        exposed[card] = True
        
    # add game state logic here
        if state == 0:
            card1 = card
            state = 1
        elif state == 1:
            card2 = card
            moves += 1
            label.set_text("Moves = "+str(moves))
            state = 2
            
        else:
            if deck[card1] != deck[card2] and state == 2:
                exposed[card1] = False
                exposed[card2] = False
            card1 = card
            state = 1
        
        print "s", state
        print "card1", deck[card1], "card2", deck[card2]
        print "moves =", moves
        print " "
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for cards in range(16):
        if exposed[cards]:
            canvas.draw_text(str(deck[cards]), [(cards * 50) + 10, 65], 50, "White")
        elif not exposed[cards]:
            canvas.draw_polygon([(cards * 50, 0), (cards * 50 + 50, 0), (cards * 50 + 50, 100), (cards * 50, 100)], 2, "Black", "Green")




# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
label = frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)


# get things rolling
frame.start()


# Always remember to review the grading rubric