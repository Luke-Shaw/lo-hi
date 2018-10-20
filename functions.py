# -*- coding: utf-8 -*-
"""
Functions for game play
"""

def new_deck():
    #outputs a classic 52 card shuffled Deck object
    
    #first get all 52 values and suits. Note diff of tile/repeat
    vals = np.tile(range(2,15),4)
    suits = np.repeat(['H','C','D','S'],13)
    #make the deck. 
    d = Deck([Card(suits[i],vals[i]) for i in range(52)])
    d.shuffle() #otherwise would be in new deck order
    
    return(d)


#example
d = new_deck()
d.show_deck()
