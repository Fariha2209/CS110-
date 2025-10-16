
#importing necessary libraries 
import stdio
import sys
import math
import stdrandom

rank = stdrandom.uniformInt(2, 15)        #Generates a number between 2 - 15 for a rank       
suit = stdrandom.uniformInt(1, 4)         #Generates a number between 1 - 4 for a suit 

#Determines the rank name based on the generated value
if rank <= 10:
    rank_name = str(rank)
elif rank == 11:
    rank_name = "Jack"
elif rank == 12:
    rank_name = "Queen"
elif rank == 13:
    rank_name = "King"
elif rank == 14: 
    rank_name = "Ace"

#Determines the suit name based on the generated value
if suit == 1:
    suit_name = "Hearts"
elif suit == 2:
    suit_name = "Diamonds"
elif suit == 3:
    suit_name = "Clubs"
elif suit == 13:
    suit_name = "Spades"

#Writes the standard output in the format "Rank of Suit"
stdio.writeln( rank_name + " of " + suit_name )




