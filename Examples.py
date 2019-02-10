# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:01:42 2018

Sandbox for testing classes/functions and playing game
"""
import random

########################
# set file location - note "path" has to be changed on diff device
import os 
path = 'C:\\Users\\my laptop\\Documents\\GitHub\\lo-hi'
os.chdir(path)

#run scripts
runfile('class-defining.py')
runfile('functions.py')

# EXAMPLES / WORKING
random.seed(0) #for shuffling consistency between runs
c1 = Card('H', 12)
c1.state_card()
c2 = Card('D', 2)
c3 = Card('C', 9)

d = Deck([c1, c2, c3])
d.show()

d.shuffle()
d.show()

d.cards[1].state_card()

dp = DiscardPile([c1,c2,c3])
dp.vis_cards()
dp.posscards #defaults to all cards
dp.reset_posscards()
dp.posscards #the above inbuilt function resets to lo-hi rules

c4 = Card('S', 14) #ACDC... c4.state_card()
dp.add_card(c4)
c5 = Card('S', 8)
dp.add_card(c5)
dp.reset_posscards()
dp.vis_cards()
dp.posscards



#Player 1
#example
random.seed(0) #so that shuffled is the same random set each time
d = new_deck()
#d.show()

#2 players at beginning of lo-hi take 5 cards each from top of deck
#discard pile starts with 1 card
p1 = Hand(d.take_card(5))
p2 = Hand(d.take_card(5))
dp = DiscardPile(d.take_card(1))

#What p1 is aware of 
p1.show_all()
dp.vis_cards()
dp.posscards #p1 can play anything

#p1 makes their move
to_play = Card('D',4)
p1.play_card(dp,to_play)
p1.show_all()
dp.vis_cards()
dp.posscards

#p2 picks up (even though they could play)
p2.show_all()
d.show(3)
p2.add_card(d)
d.show(3)
p2.show_all()





