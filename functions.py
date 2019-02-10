# -*- coding: utf-8 -*-
"""
Functions for game play
"""
import numpy as np
import random

def new_deck(shuffle=True):
    #outputs a classic 52 card shuffled Deck object
    
    #first get all 52 values and suits. Note diff of tile/repeat
    vals = np.tile(range(2,15),4)
    suits = np.repeat(['H','C','D','S'],13)
    #make the deck. 
    d = Deck([Card(suits[i],vals[i]) for i in range(52)])
    if (shuffle):
        d.shuffle() #otherwise would be in new deck order
    
    return(d)
    
def new_game(num_players = 2, seed=np.NaN):
    #starts a new game and outputs the deck, discard pile, and n players
    #TODO: think about making outputs global variables instead?? Pros/Cons?
    
    if ~np.isnan(seed): 
        random.seed(seed) #so that shuffled is the same random set each time
    
    d = new_deck()
    out = {"deck" : d}
    print(type(out))
    for i in range(num_players):
        j = str(i+1) #+1 cos python starts at 0 but we want p1, p2 not p0, p1
        out["p"+j] = Hand(d.take_card(5))
        
    dp = DiscardPile(d.take_card(1))
    out["discardpile"] = d
    return out







