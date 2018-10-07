# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 17:01:42 2018

Run class-defining.py to use test the following examples
"""


########################

runfile('class-defining.py')

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












