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
        
    def __eq__(self, other): 
        return self.__dict__ == other.__dict__    

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
    
    def take_card(self, n=1):
        #n cards are taken from top of deck
        top = self.cards[:n] #Top n cards
        self.cards = self.cards[n:] 
        #Removing the top cards from deck
        return top #outputs the top cards of the deck to caller
        
    def shuffle(self):
        #shuffle the deck
        random.shuffle(self.cards)
    
    def show(self, n=52):
        #Show the top n cards of the deck
        if n > len(self.cards):
            n = len(self.cards) #show all if n > num cards in deck
        #show the top n cards, top card first. 
        for c in self.cards[:n]:
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
        try:
            print("2nd card: ")
            self.cards[1].state_card()
        except IndexError:
            print("Doesn't exist brother: you're at the bottom of the pile")

    def show_all(self):
        #show the whole deck, top card first. 
        for c in self.cards:
            c.state_card()

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
    
    def show_all(self):
        #show all cards
        for c in self.cards:
            c.state_card()

    def add_card(self, Deck):
        #Given the Deck, take the top card
        #self.cards = Deck.take_card() + self.cards
        self.cards.extend(Deck.take_card())
        
    #discard card from hand
    def play_card(self, DiscardPile, Card):
        #play a card from the Hand into the DiscardPile
        if (Card in self.cards):
            DiscardPile.add_card(Card)
            self.cards.remove(Card)
        else:
            raise Exception('Card not in Hand')
        
        
########################









