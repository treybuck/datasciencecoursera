import random

# Rock-paper-scissors-lizard-Spock template


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

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if name == "rock":
        name = 0
    elif name == "paper":
        name = 1
    elif name == "scissors":
        name = 2
    elif name == "lizard":
        name = 3
    elif name == "Spock":
        name = 4
    else:
        print "not a valid string input"
    return name


    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if number == 0:
        number = "rock"
    elif number == 1:
        number = "paper"
    elif number == 2:
        number = "scissors"
    elif number == 3:
        number = "lizard"
    elif number == 4:
        number = "Spock"
    else:
        print "not a valid number input"
    return number
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 4, 1)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    # compute difference of comp_number and player_number modulo five
    diff = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    if diff == 0:
        winner = "Player and computer tie!"
    elif diff == 1 :
        winner = "Player wins!"
    elif diff == 2:
        winner = "Player wins!"
    else:
        winner = "Computer wins!"
    print winner
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric
