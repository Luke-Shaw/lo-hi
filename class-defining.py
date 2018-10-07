# -*- coding: utf-8 -*-
"""
Defining the classes for the game.


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
    #A deck of traditional cards
    def __init__(self, c):
        self.cards = c
    
    def take_card(self):
        #card is taken from top of deck
        top = self.cards[0] #Top Card
        self.cards = self.cards[1:(len(self.cards)+1)] 
        #Removing the top card of deck
        return top #outputs the top card of the deck to caller
        
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
    #   cards     - list of all the cards in the pile, in order
    #   posscards - vector of all integers that the card added
    #                 to the pile can be.
    
    def __init__(self, c):
        self.cards = c
        self.posscards = range(2,15) #initialise as all cards possible
                   
    def reset_posscards(self):
        #resets the possible cards that can be played
        fst = self.cards[0].value #top card of discard pile
        snd = self.cards[1].value #second...
        if (fst > snd):
            #all lower possible cards
            self.posscards = range(2, fst+1)
        else:
            if (fst < snd):
                #all higher possible cards
                self.posscards = range(fst, 15)
            else:
                if (fst == snd):
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
            self.reset_posscards() 
        else:
            #card cannot be played!
            print("*****NOT ADDED: ")
            Card.state_card()
            print("CANNOT BE PLAYED*****")
########################
            
            
            
########################
class Hand:

    def __init__(self, c):
        self.cards = c
    
    
    #take card from deck
    
    
    
    #discard card from hand
    
    
    
    
    #
