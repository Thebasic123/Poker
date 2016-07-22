
# this script is a poker dealer which deal cards depend on the
#type of game and number of players 

#!/usr/bin/env python
import random

#function transfer number to card 
#ordered by heart,diamond,spades,clubs
def numberToCard(number):
	suit = number / 13
	symbol = number % 13
	symbol = symbol + 1
	if symbol == 1:
		symbol = 'A'
	if symbol > 10 :
		if symbol == 11:
			symbol = 'J'
		elif symbol == 12:
			symbol = 'Q'
		elif symbol == 13:
			symbol = 'K'
	if suit == 0:
		suit = 'h'
	elif suit == 1:
		suit = 'd'
	elif suit == 2:
		suit = 's'
	elif suit == 3:
		suit = 'c'
	symbol = str(symbol)
	return symbol + suit

def hold_em_preflop(num_player,deck):
# each list in players contains the indexes of cards 
	count = 0
	card_count = 0
	players = {}
	print deck 
	#initialize players
	while (count < num_player):
		players[count] = []
		count = count + 1
	count = 0 
	while (card_count < 2):
		count = 0
		while (count<num_player):
			players[count].append(deck[0])
			del deck[0]
			count = count+1
		card_count = card_count + 1
	return players

def hold_em_flop(deck,board):
	print deck
	print 'burn one card'
	del deck[0]
	flop = '' + numberToCard(deck[0])+numberToCard(deck[1])+numberToCard(deck[2])
	board.extend(deck[0:3])
	del deck[0:3]
	print 'flop is ' + flop

def hold_em_turn(deck,board):
	print deck
	print 'burn one card'
	del deck[0]
	turn = '' + numberToCard(deck[0])
	board.append(deck[0])
	del deck[0]
	print 'turn is '+ turn
def hold_em_river(deck,board):
	print deck
	print 'burn one card'
	del deck[0]
	river =	'' + numberToCard(deck[0])
	board.append(deck[0])
	del deck[0]
	print 'river is '+river

#input player cards and board, determine who wins the pot
#make a list of every player's hand strength then call another function
#to compare	


#hold_em_showdown function returns hand strength of remaining players
def hold_em_showdown(players,board):
	hand_strength = {}
	#determine each player's hand strength
	for key in players:
		hand_strength[key] = []




#hold_em_winner gets input of all hand_strength and return the
#winner of the pot
#def hold_em_winner(hand_strength):


newDeck = range(0,52)
length = 52
shuffledDeck = []
#randomly swap entire list
while (len(shuffledDeck) < 52) :
	tempIndex = random.randint(0,51)
	temp = newDeck[tempIndex]
	if temp not in shuffledDeck:
		shuffledDeck.append(temp)
#deal cards for 4 players hold-em game
players = hold_em_preflop(4,shuffledDeck)
board = []
print shuffledDeck
hold_em_flop(shuffledDeck,board)
hold_em_turn(shuffledDeck,board)
hold_em_river(shuffledDeck,board)
print board
print players
for key in players:
	print key



