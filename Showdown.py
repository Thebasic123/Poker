# Using name to represent hand strength
# first element in hand strength element list 
# is hand strength,
# 0 High Card only | return all 5 cards
# 1 One Pair | return pair and 3 kickers
# 2 Two Pairs | return 2 pairs and a kicker
# 3 Three of a kind | return 3 of a kind and two kickers
# 4 Straight | return highest card
# 5 Flush | return all 5 cards
# 6 Full House | return 3 of a kind and a pair card
# 7 Quads | return quads and kicker
# 8 Straight Flush | return highest card
# 9 Royal Flush | return nothing but Royal flush 
# next 5 elements represent the best 5 cards
# For easier comparison,we put best card at the beginning.
# For example, if hand strength is A-high flush, then the second 
# element would be A of certain suit, same with other hand strengths.

# hand_strength is a dict which KEY is the index of player and 
# contains a list of information of hand

#for all hand strength functions, we input a list which 
#contains 7 cards

def isRoyalFlush(cards,strength):
	strength = []
	flush_suit = []
	suitH = []
	suitD = []
	suitS = []
	suitC = []
	for card in cards : 
		if card/13 == 0:
			suitH.append(card)
		elif card/13 == 1:
			suitD.append(card)
		elif card/13 == 2:
			suitS.append(card)
		elif card/13 == 3:
			suitC.append(card)
	if (len(suitH) >= 5):
		flush_suit = suitH
	elif (len(suitD) >= 5):
		flush_suit = suitD
	elif (len(suitS) >= 5):
		flush_suit = suitS
	elif (len(suitC) >= 5):
		flush_suit = suitC
	if flush_suit: 
		flush_suit.sort()
	else:
		return False
	for card in flush_suit:
		card = card % 13

	if((0 in flush_suit) and (9 in flush_suit) and (10 in flush_suit) and (11 in flush_suit) and (12 in flush_suit)):
		strength = [9]
		return True
	else:
		return False


def isStraightFlush(cards):
	strength = []
	flush_suit = []
	suitH = []
	suitD = []
	suitS = []
	suitC = []
	for card in cards : 
		if card/13 == 0:
			suitH.append(card)
		elif card/13 == 1:
			suitD.append(card)
		elif card/13 == 2:
			suitS.append(card)
		elif card/13 == 3:
			suitC.append(card)
	if (len(suitH) >= 5):
		flush_suit = suitH
	elif (len(suitD) >= 5):
		flush_suit = suitD
	elif (len(suitS) >= 5):
		flush_suit = suitS
	elif (len(suitC) >= 5):
		flush_suit = suitC
	if flush_suit: 
		flush_suit.sort()
	else:
		return False
	for card in flush_suit:
		card = card % 13
	#check whether there is a straight in flush suit or not
	# since cards in same suit, so no duplicates 
	counter = 0
	index = 0
	currentIndex = 0
	while index < 3:
		currentIndex = index
		counter = 0
		while counter < 5:
			if(flush_suit[currentIndex]+1 == flush_suit[currentIndex+1]):
				currentIndex++
				counter++
			else:
				break
		if (counter == 5):
			break
		index++
	if(index >= 3):
		return False
	else:
		strength = [8,flush_suit[index+4]]
		return True



def isQuads(cards,strength):
	temp = cards[:]# deep copy
	quadCard = -1
	for card in temp:
		card = card % 13
	for card in temp:
		if temp.count(card) == 4:
			strength.append(card)
			quadCard = card
			break
	#if quads exist, find kicker
	if strength:
		setDelete = [quadCard]
		temp = list(set(temp) - set(setDelete))
		temp.sort()
		#if it has Ace in list
		if (temp[0] == 0 ):
			strength.append(0)
		else:
			temp.reverse()
			strength.append(temp[0])
		strength.insert(0,7)
		return True
	else:
		return False



def isFullHose(cards,strength):
	temp = cards[:]
	threeOfAKind = -1
	pair = -1
	for card in temp :
		card = card % 13
	# find biggest three of a kind first
	for card in set(temp):
		if temp.count(card) == 3:
			#if three of a kind is Aces
			if(card == 0):
				threeOfAKind = card
				break
			elif card > threeOfAKind:
				threeOfAKind = card
	#find the best pair
	for card in set(temp):
		if (temo.count(card) >= 2) and (card != threeOfAKind):
			if(card == 0):
				pair = card
				break
			elif card > pair:
				pair = card
	if (threeOfAKind >= 0) and (pair >= 0):
		# 6 is for full house
		strength = [6,threeOfAKind,pair]
		return True
	else:
		return False


def isFlush(cards,strength):
	strength = []
	flush_suit = []
	suitH = []
	suitD = []
	suitS = []
	suitC = []
	for card in cards : 
		if card/13 == 0:
			suitH.append(card)
		elif card/13 == 1:
			suitD.append(card)
		elif card/13 == 2:
			suitS.append(card)
		elif card/13 == 3:
			suitC.append(card)
	if (len(suitH) >= 5):
		flush_suit = suitH
	elif (len(suitD) >= 5):
		flush_suit = suitD
	elif (len(suitS) >= 5):
		flush_suit = suitS
	elif (len(suitC) >= 5):
		flush_suit = suitC
	if flush_suit: 
		flush_suit.sort()
		# if the first element is not Ace, then use the current order
		# otherwise, put ace as the biggest
		if flush_suit[0] % 13 == 0:
			strength.append(flush_suit[0])
			del flush_suit[0]
			flush_suit.reverse()
			strength.extend(flush_suit[0:4])
		else:
			flush_suit.reverse()
			strength.extend(flush_suit[0:5])
			
		strength.insert(0,5)#add hand strength at the top of list 
		return True
	else:
		return False

def isStraight(cards,strength):
	temp = cards[:]
	#highest card in straight
	highest = -1
	for card in temp:
		card = card % 13
	temp = set(temp)
	temp = sorted(temp)
	counter = 0
	index = 0
	currentIndex = 0
	#check 10 to Ace straight first
	if((0 in temp) and (9 in temp) and (10 in temp) and (11 in temp) and (12 in temp)):
		strength = [4,0]
		return True
	else:
		while index < 3:
			currentIndex = index
			counter = 0
			while counter < 5:
				if(temp[currentIndex]+1 == temp[currentIndex+1]):
					currentIndex++
					counter++
				else:
					break
			if (counter == 5):
				break
			index++
		if(index >= 3):
			return False
		else:
			strength = [4,temp[index+4]]
			return True
def isThreeOfAKind(cards,strength):
	temp = cards[:]
	threeOfAKind = -1
	kickerOne = -1
	kickerTwo = -1
	for card in temp:
		card = card % 13
	for card in set(temp):
		if(temp.count(card)==3):
			if(card == 0):
				threeOfAKind = 0
				break
			else:
				if(card > threeOfAKind):
					threeOfAKind = card
	if(threeOfAKind == -1):
		return False
	else:
		temp = set(temp)
		temp = sorted(temp)
		index = temp.index(threeOfAKind)
		del temp[index]
		if(temp[0] == 0):
			strength = [3,threeOfAKind,0,temp[-1]]
		else:
			strength = [3,threeOfAKind,temp[-1],temp[-2]]
		return True
def isTwoPairs(cards,strength):
	temp = cards[:]
	#it might contain 3 pairs, we use a list find the best two 
	pairs = [] 
	kicker = -1
	for card in temp :
		card = card % 13
	for card in set(temp):
		if(temp.count(card) == 2):
			pairs.append(card)

	#find the best two pairs 
	if(len(pairs) < 2):
		return False
	if(len(pairs) > 2):
		pairs.sort()
		if(pairs[0]==0):
			pairs = pairs[0:2]
		else:
			pairs = pairs[-2:]

	#delete pair elements from temp then find kicker
	temp = set(temp)
	temp = sorted(temp)
	indexOne = temp.index(pairs[0])
	indexTwo = temp.index(pairs[1])
	del temp[indexOne]
	del temp[indexTwo]
	if(temp[0] == 0):
		kicker = 0
		strength = [2,pairs[0],pairs[1],kicker]
	else:
		kicker = temp[-1]
		strength = [2,pairs[0],pairs[1],kicker]
	return True

def isOnePair(cards,strength):
	temp = cards[:]
	pair = -1
	for card in temp :
		card = card % 13
	for card in set(temp):
		if(temp.count(card) == 2):
			pair = card
			break # since we run two pair function first, so it has one pair most
	if(pair == -1):
		return False
	temp = set(temp)
	temp = sorted(temp)
	index = temp.index(pair)
	del temp[index]
	#find kickers for pair
	if(temp[0] == 0):
		strength = [1,pair,0,temp[-1],temp[-2]]
	else:
		strength = [1,pair,temp[-1],temp[-2],temp[-3]]
	return True

#since High card is the last function we run, we won't return boolean value
def highCard(cards,strength):
	temp = cards[:]
	temp = sorted(temp)
	if(temp[0] == 0):
		strength = [0]+[0]+temp[-4:]
	else:
		strength = [0]+temp[-5:]






#hold_em_showdown function returns hand strength of remaining players
def hold_em_showdown(players,board):
	hand_strength = {}
	#determine each player's hand strength
	for key in players:
		hand_strength[key] = []
		seven_cards = []
		seven_cards = players[key] + board

		#Determine hand strength from best to the worst
		#we use functions to determine hand strength 