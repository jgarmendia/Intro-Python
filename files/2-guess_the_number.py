# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
secret_number = 0
remaining = 7

    

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    global secret_number, remaining
    secret_number = random.randrange(0, 100)
    remaining = 7
    print "New Game. Range is 0 to 100"
    print "Number of remaining guesses is 7"
    print " "
    

    
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global secret_number, remaining
    secret_number = random.randrange(0, 1000)
    remaining = 10
    print "New Game. Range is 0 to 1000"
    print "Number of remaining guesses is 10"
    print " "
    

    
def get_input(guess):
    # main game logic goes here	
    global secret_number, remaining
    guess = int(guess)
    if guess < secret_number:
        print "Your guess was", guess
        print "Higher!"
        remaining += -1
        print "You have", remaining, "remain(s)"
        print " "
    elif guess > secret_number:
        print "Your guess was", guess
        print "Lower!"
        remaining += -1
        print "You have", remaining, "remain(s)"
        print " "
    elif guess == secret_number:
        print "Your guess was", guess
        print "Correct, you win with", remaining, "remain(s)."
        print " "
        range100()
    else:
        print "Restart the game"
    if remaining == 0:
        print "You lose, secret number was", secret_number
        print " "
        range100()
        
  
    
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
frame.add_button("Range 0 to 100", range100, 200)
frame.add_button("Range 0 to 1000", range1000, 200)
frame.add_input("Enter your guess", get_input, 200)

# start frame
frame.start()
range100()