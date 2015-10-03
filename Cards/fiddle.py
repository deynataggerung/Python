import pygame
import copy
from random import randint

#A class defining properties of each card
#Add a property that is passed in from the creation identifying the card as part of a deck.
#Make sure that the individual hands are described with list so the cards stay constantly in the same place.
class Card(object):
	suit_hierarchy = {"c": 3,"d": 2,"h": 1,"s": 0}
	possible_cards = ['3','4','5','6','7','8','9','10',"j","q","k","a",'2']
	def __init__(self, value, suit):
		self.suit = suit
		self.identifier = "%s%s" % (Card.possible_cards[value-1], self.suit[0])
		self.value = value*4 -Card.suit_hierarchy[self.suit[0]]
		self.image = pygame.image.load("images\\%s.png" %(self.identifier))
	
	#Function to display image to screen
	#def 


#A class defining an entire deck. Contains Card() Objects
class Deck(object):
	suits = ["clubs", "diamonds", "hearts", "spades"]
	def __init__(self):
		self.size = 52
		self.cards = {}
		for f in Deck.suits:
			for i in range(1,14):
				self.cards[Card(i, f).identifier] = Card(i,f)

		#A list of the keys for easy referencing of the deck
		self.reference = self.cards.keys()
		for i in range(20):
			self.shuffle()
			
	#Returns a random card
	def pick_a_card(self):
		return self.cards[self.reference[randint(0,len(self.reference)-1)]]
	
	#Returns a copy of the reference list
	def get_reference(self):
		return copy.copy(self.reference)

	def shuffle(self):
		for i in range(300):
			#Takes a random card out and then puts it back in a random place.
			self.reference.insert(randint(0,len(self.reference)-1), self.reference.pop(randint(0,len(self.reference)-1)))

	#"Deals" the cards into as many hands as specified (only 4 atm)
	def deal(self, player_count):
		self.shuffle()
		self.hand_size = len(self.reference)/player_count
		self.hand1 = self.reference[0:self.hand_size]
		self.hand2 = self.reference[self.hand_size:self.hand_size*2]
		self.hand3 = self.reference[self.hand_size*2:self.hand_size*3]
		self.hand4 = self.reference[self.hand_size*3:]

	def rearrange(self, chosen):
		#Copy the original so I don't screw it up
		subject = copy.copy(chosen)
		#Set up the new ordered list with the first card
		arranged = []
		arranged.append(subject.pop())
		
		#Keeps picking new cards out till the list is empty
		while len(subject) >= 1:
			#Take out the card to be placed
			single = subject.pop()
			place = 0
			greater = True
			#This while loop checks the picked card against the first card in the list. If greater it check the next one until it finds a card that is greater than itself. At this point it exits with the index the card belongs.
			while greater:
				if self.cards[single].value < self.cards[arranged[place]].value:
					greater = False
				elif self.cards[single].value > self.cards[arranged[place]].value:
					place += 1
				else:
					print "you screwed up"
					greater = False

				if place == len(arranged):
					greater = False
			#Place the card in it's correct spot
			arranged.insert(place, single)

	def display_hand(self, hand_num):
		screen.fill(darkgreen)
		if hand_num == 1:
			#hand in question
			hiq = self.hand1
		if hand_num == 2:
			hiq = self.hand2
		if hand_num == 3:
			hiq = self.hand3
		if hand_num == 4:
			hiq = self.hand4


		#Don't screw up on uno
		num = len(hiq)
		if num == 1:
			screen.blit(self.cards[hiq[0]].image(), align(self.cards[hiq[0]].image(), "bottom", "center"))
		else:
			#Even hands have an imaginary pivot card
			if num %2 == 0:
				first_half = hiq[0: num/2-1]
				second_half = hiq[num/2+2:]
				pivot = pygame.Rect(align(self.cards[hiq[0]].image(), "bottom", "center"), (168,243))
				lpivot = (hiq[num/2], offset(pivot, -0.1, "horizontal", (pivot.x, pivot.y)))
				rpivot = (hiq[num/2+1], offset(pivot, 0.1, "horizontal", (pivot.x, pivot.y)))
				ldistance = num*-0.2-0.1
				rdistance = 0.1
			elif num%2 == 1:
				first_half = hiq[0: num/2]
				second_half = hiq[num/2:]
				print hiq[num/2+1]
				pivot = self.cards[hiq[num/2+1]].image()
				lpivot = (pivot, align(self.cards[hiq[num/2]].image(), "bottom", "center"))
				rpivot = (pivot, align(self.cards[hiq[num/2]].image(), "bottom", "center"))
				ldistance = num*-0.2
				rdistance = 0
		
			for i in range(len(first_half)):
				screen.blit(self.cards[first_half[i]].image(), offset(pivot, ldistance+i*0.2, (pivot.x, pivot.y)))
			screen.blit(lpivot)
			screen.blit(rpivot)
			for i in range(len(second_half)):
				screen.blit(self.cards[second_half[i]].image(), offset(pivot, rdistance+num*0.2, (pivot.x, pivot.y)))


#Make a function that will center an image in the screen
def align(image1, vert_align="center", horiz_align="center", image2=False, image2_pos=(0,0)):
	
	#Determine what type of input was given and then produce the correct size
	if isinstance(image1, tuple):
		width, height = image1
	elif hasattr(image1, "get_size"):
		width, height = image1.get_size()
	else:
		width, height = (0,0)
		#try:
			#width, height = pygame.font.size()
		#except AttributeError:
			#width, height = (0,0)

	image2_x, image2_y = image2_pos
	overall_width = screen.get_width()
	overall_height = screen.get_height()
	if isinstance(image2,tuple):
		overall_width, overall_height = image2
	elif image2:
		overall_width = image2.get_width()
		overall_height = image2.get_height()

	if isinstance(image2_pos, tuple):
		if horiz_align == "center":
			x_comp = image2_x+overall_width/2-width/2
		elif horiz_align == "right":
			x_comp = image2_x+overall_width-width
		elif horiz_align == "left":
			x_comp = image2_x
		else:
			x_comp = 0

		if vert_align == "center":
			y_comp = image2_y+overall_height/2-height/2
		elif vert_align == "top":
			y_comp = image2_y
		elif vert_align == "bottom":
			y_comp = image2_y+overall_height-height
		else:
			y_comp = 0 

	else:
		x_comp = 0
		y_comp = 0
	return (x_comp, y_comp)

# A standard function for positioning an image relative to coordinates
def offset(model_image, magnitude, direction, org_coord):
	x_comp, y_comp = org_coord
	if direction == "vertical":
		if isinstance(magnitude, int):
			y_comp += magnitude
		elif isinstance(magnitude, float):
			y_comp += magnitude*model_image.get_height()
		else:
			pass
	elif direction == "horizontal":
		if isinstance(magnitude, int):
			x_comp += magnitude
		elif isinstance(magnitude, float):
			x_comp += magnitude*model_image.get_width()
		else:
			pass
	elif direction == "both":
		if isinstance(magnitude, int):
			x_comp += magnitude
			y_comp += magnitude
		elif isinstance(magnitude, float):
			x_comp += magnitude*model_image.get_width()
			y_comp += magnitude*model_image.get_height()
		else:
			pass
	else:
		pass
	return (x_comp, y_comp)
