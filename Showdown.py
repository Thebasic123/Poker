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


def isStraightFlush(cards,strength):
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
				currentIndex += 1
				counter += 1
			else:
				break
		if (counter == 5):
			break
		index += 1
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
		if (temp.count(card) >= 2) and (card != threeOfAKind):
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
					currentIndex += 1
					counter += 1
				else:
					break
			if (counter == 5):
				break
			index += 1
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


#function gets a dict of hand strength with player index as key
#return winner index 
# two or more players might have same hands, so we return a list of indexes 
def getWinner(hand_strength):
	#get best hand_rank first
	best = 0
	current = 0
	best_hands = {}
	result = []
	for key in hand_strength:
		current = hand_strength[key][0]
		if(current > best):
			best = current
	#get all hands in best ranking 
	for key in hand_strength:
		if(hand_strength[key][0] == best):
			best_hands[key] = hand_strength[key]

	#find the best hand in best ranking
	#if best hand is royal flush, return all keys
	if(best == 9):
		return best_hands.keys()
	elif(best == 8):
		best_SF_card = 0
		for key in best_hands:
			if(best_SF_card < best_hands[key][1]):
				best_SF_card = best_hands[key][1]
		for key in best_hands:
			if(best_SF_card == best_hands[key][1]):
				result.append(key)
		return result
	elif(best == 7):
		best_quads = -1
		best_kicker = -1 #best kicker only gets kicker for best quads
		#get best quads first
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_quads = 0
				break
			if(best_hands[key][1] > best_quads):
				best_quads = best_hands[key][1]

		#get best kicker
		for key in best_hands:
			if(best_hands[key][2] == best_quads):
				if(best_hands[key][2] == 0):
					best_kicker = 0
					break
				elif(best_hands[key][2] > best_kicker):
					best_kicker = best_hands[key][2]
		#get winners 
		for key in best_hands:
			if(best_hands[key][1]==best_quads and best_hands[key][2]==best_kicker):
				result.append(key)
		return result
	elif(best == 6):
		best_FH_three = -1
		best_FH_pair = -1
		#get best three of a kind in FH first
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_FH_three = 0
				break
			if(best_hands[key][1] > best_FH_three):
				best_FH_three = best_hands[key][1]
		#get best pair for best three of a kind 
		for key in best_hands:
			if(best_hands[key][1] == best_FH_three):
				if(best_hands[key][2] == 0):
					best_FH_pair = 0
					break
				elif(best_hands[key][2] > best_FH_pair):
					best_FH_pair = best_hands[key][2]
		#get winners 
		for key in best_hands:
			if(best_hands[key][1]==best_FH_three and best_hands[key][2]==best_FH_pair):
				result.append(key)
		return result
	elif(best == 5):
		best_FcardOne = -1
		best_FcardTwo = -1
		best_FcardThree = -1
		best_FcardFour = -1
		best_FcardFive = -1
		#find the best cardOne 
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_FcardOne = 0
				break
			if(best_hands[key][1] > best_FcardOne):
				best_FcardOne = best_hands[key][1]
		#find the best cardTwo
		for key in best_hands:
			if(best_hands[key][1] == best_FcardOne):
				if(best_hands[key][2] > best_FcardTwo):
					best_FcardTwo = best_hands[key][2]
		#find the best cardThree
		#can't be ace
		for key in best_hands:
			if(best_hands[key][1] == best_FcardOne):
				if(best_hands[key][2] == best_FcardTwo):
					if(best_hands[key][3] > best_FcardThree):
						best_FcardThree = best_hands[key][3]
		#find the best cardFour
		for key in best_hands:
			if(best_hands[key][1] == best_FcardOne):
				if(best_hands[key][2] == best_FcardTwo):
					if(best_hands[key][3] == best_FcardThree):
						if(best_hands[key][4] > best_FcardFour):
							best_FcardFour = best_hands[key][4]
		#find the best cardFive
		for key in best_hands:
			if(best_hands[key][1] == best_FcardOne):
				if(best_hands[key][2] == best_FcardTwo):
					if(best_hands[key][3] == best_FcardThree):
						if(best_hands[key][4] == best_FcardFour):
							if(best_hands[key][5] > best_FcardFive):
								best_FcardFive = best_hands[key][5]
		#find the best hands
		for key in best_hands:
			if(best_hands[key][1] == best_FcardOne and best_hands[key][2] == best_FcardTwo and best_hands[key][3] == best_FcardThree 
				and best_hands[key][4] == best_FcardFour and best_hands[key][5] == best_FcardFive):
				result.append(key)
		return result
	elif(best == 4):
		best_S_card = 0
		for key in best_hands:
			if(best_S_card < best_hands[key][1]):
				best_S_card = best_hands[key][1]
		for key in best_hands:
			if(best_S_card == best_hands[key][1]):
				result.append(key)
		return result
	elif(best == 3):
		best_three = -1
		best_three_kickerOne = -1
		best_three_kickerTWo = -1
		#find best three of a kind
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_three = 0
				break
			if(best_hands[key][1] > best_three):
				best_three = best_hands[key][1]
		#find best kicker one
		for key in best_hands:
			if(best_hands[key][1] == best_three):
				if(best_hands[key][2] == 0):
					best_three_kickerOne = 0
					break
				if(best_hands[key][2] > best_three_kickerOne):
					best_three_kickerOne = best_hands[key][2]

		#find best kicker two
		#since we have two kickers, so the worse kicker can't be Ace
		for key in best_hands:
			if(best_hands[key][1] == best_three):
				if(best_hands[key][2] == best_three_kickerOne):
					if(best_hands[key][3] > best_three_kickerTWo):
						best_three_kickerTWo = best_hands[key][3]
		#find the best hands
		for key in best_hands:
			if(best_hands[key][1] == best_three and best_hands[key][2] == best_three_kickerOne and best_hands[key][3] == best_three_kickerTWo):
				result.append(key)
		return result
	elif(best == 2):
		best_pairOne = -1
		best_pairTwo = -1
		best_twoPair_kicker = -1
		#find best pair one
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_pairOne = 0
				break
			if(best_hands[key][1] > best_pairOne):
				best_pairOne = best_hands[key][1]
		#find best pair two
		#it can't be ace
		for key in best_hands:
			if(best_hands[key][1] == best_pairOne):
				if(best_hands[key][2] > best_pairTwo):
					best_pairTwo = best_hands[key][2]
		#find best kicker for two pairs
		for key in best_hands:
			if(best_hands[key][1] == best_pairOne):
				if(best_hands[key][2] == best_pairTwo):
					if(best_hands[key][3] == 0):
						best_twoPair_kicker = 0
						break
					if(best_hands[key][3] > best_twoPair_kicker):
						best_twoPair_kicker = best_hands[key][3]
		#find the best hands
		for key in best_hands:
			if(best_hands[key][1] == best_pairOne and best_hands[key][2] == best_pairTwo and best_hands[key][3] == best_twoPair_kicker):
				result.append(key)
		return result
	elif(best == 1):
		best_pair = -1
		best_pair_kickerOne = -1
		best_pair_kickerTwo = -1
		best_pair_kickerThree = -1
		best_pair_kickerFour = -1
		#find the best pair 
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_pair = 0
				break
			if(best_hands[key][1] > best_pair):
				best_pair = best_hands[key][1]
		#find the best kickerOne
		for key in best_hands:
			if(best_hands[key][1] == best_pair):
				if(best_hands[key][2] == 0):
					best_pair_kickerOne = 0
					break
				if(best_hands[key][2] > best_pair_kickerOne):
					best_pair_kickerOne = best_hands[key][2]
		#find the best kickerTwo
		#can't be ace
		for key in best_hands:
			if(best_hands[key][1] == best_pair):
				if(best_hands[key][2] == best_pair_kickerOne):
					if(best_hands[key][3] > best_pair_kickerTwo):
						best_pair_kickerTwo = best_hands[key][3]
		#find the best kickerThree
		for key in best_hands:
			if(best_hands[key][1] == best_pair):
				if(best_hands[key][2] == best_pair_kickerOne):
					if(best_hands[key][3] == best_pair_kickerTwo):
						if(best_hands[key][4] > best_pair_kickerThree):
							best_pair_kickerThree = best_hands[key][4]
		#find the best hands
		for key in best_hands:
			if(best_hands[key][1] == best_pair and best_hands[key][2] == best_pair_kickerOne and best_hands[key][3] == best_pair_kickerTwo 
				and best_hands[key][4] == best_pair_kickerThree):
				result.append(key)
		return result
	elif(best == 0):
		best_cardOne = -1
		best_cardTwo = -1
		best_cardThree = -1
		best_cardFour = -1
		best_cardFive = -1
		#find the best cardOne 
		for key in best_hands:
			if(best_hands[key][1] == 0):
				best_cardOne = 0
				break
			if(best_hands[key][1] > best_cardOne):
				best_cardOne = best_hands[key][1]
		#find the best cardTwo
		for key in best_hands:
			if(best_hands[key][1] == best_cardOne):
				if(best_hands[key][2] > best_cardTwo):
					best_cardTwo = best_hands[key][2]
		#find the best cardThree
		#can't be ace
		for key in best_hands:
			if(best_hands[key][1] == best_cardOne):
				if(best_hands[key][2] == best_cardTwo):
					if(best_hands[key][3] > best_cardThree):
						best_cardThree = best_hands[key][3]
		#find the best cardFour
		for key in best_hands:
			if(best_hands[key][1] == best_cardOne):
				if(best_hands[key][2] == best_cardTwo):
					if(best_hands[key][3] == best_cardThree):
						if(best_hands[key][4] > best_cardFour):
							best_cardFour = best_hands[key][4]
		#find the best cardFive
		for key in best_hands:
			if(best_hands[key][1] == best_cardOne):
				if(best_hands[key][2] == best_cardTwo):
					if(best_hands[key][3] == best_cardThree):
						if(best_hands[key][4] == best_cardFour):
							if(best_hands[key][5] > best_cardFive):
								best_cardFive = best_hands[key][5]
		#find the best hands
		for key in best_hands:
			if(best_hands[key][1] == best_cardOne and best_hands[key][2] == best_cardTwo and best_hands[key][3] == best_cardThree 
				and best_hands[key][4] == best_cardFour and best_hands[key][5] == best_cardFive):
				result.append(key)
		return result


#hold_em_showdown function returns hand strength of remaining players
def hold_em_showdown(players,board):
	hand_strength = {}
	#determine each player's hand strength
	for key in players:
		hand_strength[key] = []
		seven_cards = []
		seven_cards = players[key] + board
		print seven_cards
		if isRoyalFlush(seven_cards,hand_strength[key]):
			continue
		elif isStraightFlush(seven_cards,hand_strength[key]):
			continue
		elif isQuads(seven_cards,hand_strength[key]):
			continue
		elif isFullHose(seven_cards,hand_strength[key]):
			continue
		elif isFlush(seven_cards,hand_strength[key]):
			continue
		elif isStraight(seven_cards,hand_strength[key]):
			continue
		elif isThreeOfAKind(seven_cards,hand_strength[key]):
			continue
		elif isTwoPairs(seven_cards,hand_strength[key]):
			continue
		elif isOnePair(seven_cards,hand_strength[key]):
			continue
		else:
			highCard(seven_cards,hand_strength[key])
	print hand_strength
	winners = []
	winners = getWinner(hand_strength)
	print winners


		#Determine hand strength from best to the worst
		#we use functions to determine hand strength 