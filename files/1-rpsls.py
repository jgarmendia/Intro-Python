# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    """ change the imput number to a name"""
    if number == 0:
        number = "rock"
    elif number == 1:
            number = "Spock"
    elif number == 2:
                number = "paper"
    elif number == 3:
                    number = "lizard"
    elif number == 4:
                        number = "scissors"
    else: print "number error"
    return number
                    
                
    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    """change the imput name to a number"""
    if name == "rock":
        name = 0
    elif name == "Spock":
            name = 1
    elif name == "paper":
                name = 2
    elif name == "lizard":
                    name = 3
    elif name == "scissors":
                        name = 4
    else: print "name error"
    return name
    
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name):
    """compares the result of the difference 
    in the player's choices and the computer 
    to determine and print the winner"""
    player_number = name_to_number(name)
    comp_number = random.randrange(0, 5)
    diff = (player_number - comp_number) % 5
    if (diff == 1) or (diff == 2):
        print "Player chooses" , number_to_name(player_number)
        print "Computer chooses" , number_to_name(comp_number)
        print "Player wins!"
        print " "
    elif (diff == 3) or (diff == 4):
        print "Player chooses" , number_to_name(player_number)
        print "Computer chooses" , number_to_name(comp_number)
        print "Computer wins!"
        print " "
    else:
        print "Player chooses", number_to_name(player_number)
        print "Computer chooses" , number_to_name(comp_number)
        print "Tie!"
        print " "

        
        


    
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


