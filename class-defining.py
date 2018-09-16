# -*- coding: utf-8 -*-
"""
Defining the classes for the game, with example of 
in action at the end.

Most recent update: DiscardPile class
                    ^^^ still needs work, posscards
                        working but more to be added

"""
########################
#import itertools
import random
#import numpy as np
########################



########################
class Card:
    #a single traditional playing card
    def __init__(self, s, v):
        self.suit = s
        self.value = v
    

    def state_card(self):
    #state_card outputs in "proper english" what the card is
        #first the suit
        if(self.suit == 'H'): 
            suitfull = 'Hearts'
        if(self.suit == 'C'): 
            suitfull = 'Clubs'
        if(self.suit == 'D'): 
            suitfull = 'Diamonds'
        if(self.suit == 'S'): 
            suitfull = 'Spades'
        #then the special values
        valuefull = str(self.value)
        if(self.value == 11):
            valuefull = 'Jack'
        if(self.value == 12):
            valuefull = 'Queen'
        if(self.value == 13):
            valuefull = 'King'
        if(self.value == 14):
            valuefull = 'Ace' #note ace is high so not 1
    
        #print the result
        print('The ' + valuefull + ' of ' + suitfull)
########################



########################
class Deck:
    #a deck of traditional cards
    def __init__(self, c):
        self.cards = c
    
    def add_card(self, Card):
        #card is added to top of deck
        self.cards = [Card] + self.cards #list adding
        
    def shuffle(self):
        #shuffle the deck
        random.shuffle(self.cards)
    
    def show_deck(self):
        #show the whole deck, top card first. 
        for c in self.cards:
            c.state_card()
########################



########################
class DiscardPile:
    #the face up cards used in lo-hi gameplay
    #items:
    #   cards     list of all the cards in the pile, in order
    #   posscards vector of all integers that the card added
    #             to the pile can be.
    def __init__(self, c):
        self.cards = c
        self.posscards = range(2,15) #initialise as all cards possible
                   
    def reset_posscards(self):
        #resets the possible cards that can be played
        fst = self.cards[0].value
        snd = self.cards[1].value
        if (fst > snd):
            #all lower possible cards
            self.posscards = range(2, fst+1)
        else:
            if (fst < snd):
                #all higher possible cards
                self.posscards = range(fst, 15)
                
        if ((fst in [2,14]) or (fst == snd)):
            #special case where any can be played
            self.posscards = range(2,15)

    def vis_cards(self):
        #show the 2 visible cards
        print("Top card: ")
        self.cards[0].state_card()
        print("2nd card: ")
        self.cards[1].state_card()

    def add_card(self, Card):
        #adds a card to the top, IF valid in lo-hi gameplay
        if (Card.value in self.posscards):
            self.cards = [Card] + self.cards
        else:
            #card cannpt be played!
            print("*****NOT ADDED: ")
            Card.state_card()
            print("CANNOT BE PLAYED*****")
########################



########################
#EXAMPLES / WORKING
c1 = Card('H', 12)
c1.state_card()
c2 = Card('D', 2)
c3 = Card('C', 9)

d = Deck([c1, c2])

d.show_deck()

d.add_card(c3)

d.show_deck()
d.shuffle()
d.show_deck()

d.cards[1].state_card()


c1 = Card('H', 12)
c2 = Card('D', 2)
c3 = Card('C', 9)
dp = DiscardPile([c1,c2,c3])
dp.vis_cards()
dp.posscards #defaults to all cards
dp.reset_posscards()
dp.posscards #the above inbuilt function resets to lo-hi rules

c4 = Card('S', 14) #ACDC... c4.state_card()
dp.add_card(c4)
c5 = Card('S', 8)
dp.add_card(c5)
dp.reset_posscards
dp.vis_cards()
dp.posscards












