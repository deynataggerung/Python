import pygame
import copy
from sys import argv
from random import randint


#Next to work on is making the AI play next highest card. In the screen section make it display the arrow image depending on whose turn it is. Arrow1, Arrow2, Arrow3 and Arrow4. Then make the image loaded individually with the number from turn as a %s

#A class defining properties of each card
#Add a property that is passed in from the creation identifying the card as part of a deck.
#Make sure that the individual hands are described with list so the cards stay constantly in the same place.
class Card(object):
	suit_hierarchy = {"k":10,"c": 3,"d": 2,"h": 1,"s": 0}
	possible_cards = ['3','4','5','6','7','8','9','10',"j","q","k","a",'2',"bac"]
	def __init__(self, value, suit):
		self.suit = suit
		self.identifier = "%s%s" % (Card.possible_cards[value-1], self.suit[0])
		self.value = value*4 -Card.suit_hierarchy[self.suit[0]]
		self.image = resize(pygame.image.load("images\\%s.png" %(self.identifier)),0.8)
		self.position = (0,0)
		self.hitbox = pygame.Rect(0,0,20,20)
		if self.identifier == "back":
			self.value = -1
	
	#Function to display image to screen

	#
	def update_pos(self, coord, offset = 0.2):
		try:
			self.position = coord
			self.hitbox = pygame.Rect(self.position, (self.image.get_width()*offset, self.image.get_height()))
		except TypeError:
			print "bad input on update_pos"



#A class defining an entire deck. Contains Card() Objects
class Deck(object):
	suits = ["clubs", "diamonds", "hearts", "spades"]
	def __init__(self):
		self.size = 52
		self.cards = {}
		#Create Instances of each card in the deck
		for f in Deck.suits:
			for i in range(1,14):
				self.cards[Card(i, f).identifier] = Card(i,f)
		self.backside = Card(14, "k")
		#A list of the keys for easy referencing of the deck
		self.reference = self.cards.keys()
		self.final_hover = []
		self.played = "back"
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
		self.hands = [self.reference[0:self.hand_size], self.reference[self.hand_size:self.hand_size*2], self.reference[self.hand_size*2:self.hand_size*3], self.reference[self.hand_size*3:]]
		for i in self.hands:
			self.rearrange(i)

	def rearrange(self, chosen):
		#Set up the new ordered list with the first card
		arranged = []
		arranged.append(chosen.pop())
		
		#Keeps picking new cards out till the list is empty
		while len(chosen) >= 1:
			#Take out the card to be placed
			single = chosen.pop()
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
		while len(arranged) >=1:
			chosen.append(arranged.pop())
		chosen.reverse()

	def display_hand(self, hand_num = 1):
		screen.fill(darkgreen)
		hand = self.hands[hand_num-1]
		num = len(hand)
		height = self.cards[hand[0]].image.get_height()
		width = self.cards[hand[0]].image.get_width()
		if num == 1:
			screen.blit(self.cards[hand[0]].image, align(self.cards[hand[0]].image, "bottom", "center"))
		else:
			first = align((width+(width*0.2*num), height), "bottom", "center")
			c = 0
			x, y = first
			for i in hand:
				v = 0
				if i in self.final_hover:
					v = height*0.4
				the_coordinates = (x+width*0.2*c, y-v)
				screen.blit(self.cards[i].image, (the_coordinates))
				self.cards[i].update_pos(the_coordinates)
				if c == num-1:
					self.cards[i].update_pos(the_coordinates, 1)
				c +=1

		h2 = resize(pygame.image.load("images\\hand2.png"),0.8)
		h3 = resize(pygame.image.load("images\\hand3.png"),0.8)
		h4 = resize(pygame.image.load("images\\hand4.png"),0.8)
		screen.blit(h2, align(h2, "center", "left"))
		screen.blit(h3, align(h3, "top", "center"))
		screen.blit(h4, align(h4, "center", "right"))
		pygame.display.flip()



	#Tests to see if the mouse is hovering over a card
	def hover(self, coord):
		check = self.hands[0]
		for n in check:
			#Card in question
			ciq = self.cards[n]
			if ciq.hitbox.collidepoint(coord):
				if ciq.identifier in self.final_hover:
					self.final_hover.remove(ciq.identifier)
				else:
					self.final_hover.append(ciq.identifier)
	#only removes 1. Work on that
	def play(self):
		self.played_cards = []
		played_cards2 = []
		c = 0
		while len(self.final_hover) > 0:
			self.hands[0].remove(self.final_hover[c])
			self.played_cards.append(self.final_hover[c])
			self.final_hover.remove(self.final_hover[c])
		for i in self.played_cards:
			played_cards2.append(self.cards[i])
		return played_cards2



class Slave(object):
	def __init__(self, deck):
		self.pile = deck.backside
		self.deck = deck
		self.turn = 1
	
	def is_valid(self, chosen):
		if len(chosen) == 1:
			if chosen[0].value > self.pile.value:
				self.pile = chosen[0]
				self.turn +=1
			elif chosen[0].value < self.pile.value:
				self.invalid(chosen)
		elif len(chosen) > 1:
			self.invalid(chosen)
			
		print self.pile.identifier

	def invalid(self, returns):
		for i in returns:
			self.deck.hands[0].append(i.identifier)
			self.deck.rearrange(self.deck.hands[0])




class Screen(object):
	def __init__(self, deck, rules):
		self.deck = deck
		self.rules = rules
		self.screen = pygame.display.set_mode((1000,800))
		
	def display(self, hand_num = 1):
		self.screen.fill(darkgreen)
		hand = self.deck.hands[hand_num-1]
		num = len(hand)
		height = self.deck.cards[hand[0]].image.get_height()
		width = self.deck.cards[hand[0]].image.get_width()
		if num == 1:
			self.screen.blit(self.cards[hand[0]].image, align(self.cards[hand[0]].image, "bottom", "center"))
		else:
			first = align((width+(width*0.2*num), height), "bottom", "center")
			c = 0
			x, y = first
			for i in hand:
				v = 0
				if i in self.deck.final_hover:
					v = height*0.4
				the_coordinates = (x+width*0.2*c, y-v)
				self.screen.blit(self.deck.cards[i].image, (the_coordinates))
				self.deck.cards[i].update_pos(the_coordinates)
				if c == num-1:
					self.deck.cards[i].update_pos(the_coordinates, 1)
				c +=1
		
		self.display_other_hands()
		self.display_played()
		self.display_turn()

	def display_other_hands(self):
		h2 = resize(pygame.image.load("images\\hand2.png"),0.8)
		h3 = resize(pygame.image.load("images\\hand3.png"),0.8)
		h4 = resize(pygame.image.load("images\\hand4.png"),0.8)
		self.screen.blit(h2, align(h2, "center", "left"))
		self.screen.blit(h3, align(h3, "top", "center"))
		self.screen.blit(h4, align(h4, "center", "right"))

	def display_played(self):
		self.screen.blit(self.rules.pile.image, align(prototype.image, "center","center"))
		pygame.display.flip()
	
	def display_turn(self):
		arrow =resize(pygame.image.load("images\\arrow.png"), 0.2)
		self.screen.blit(arrow, align(arrow))
		


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
	overall_width = The_Screen.screen.get_width()
	overall_height = The_Screen.screen.get_height()
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
			y_comp -= magnitude
		elif isinstance(magnitude, float):
			y_comp -= magnitude*model_image.get_height()
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
			y_comp -= magnitude
		elif isinstance(magnitude, float):
			x_comp += magnitude*model_image.get_width()
			y_comp -= magnitude*model_image.get_height()
		else:
			pass
	else:
		pass
	return (x_comp, y_comp)
	
def resize(orig, magnitude):
	x_comp, y_comp = orig.get_size()
	x_comp = int(x_comp*magnitude)
	y_comp = int(y_comp*magnitude)
	return pygame.transform.scale(orig, (x_comp, y_comp))

def value(event):
	return pygame.key.name(event.key)

#It's important to start sometime
pygame.init()

#Create Instances of my Classes
The_Deck = Deck()
The_Rules = Slave(The_Deck)
The_Screen = Screen(The_Deck, The_Rules)

#Defining colors for screen
black = (0,0,0)
white = (255,255,255)
green = (0,255,255)
darkgreen = (10,104,0)
brown = (127, 55, 0)


#Fonts
text = pygame.font.Font("unrealised.ttf", 120)

#Conditions for Starting
choosing = True
playing = True
hand = 1
prototype = Card(1, "spades")

clock = pygame.time.Clock()
start_button = pygame.Rect(align((500,200)), (500,200))

The_Screen.screen.fill(darkgreen)
pygame.draw.rect(The_Screen.screen, black, start_button, 3)
game_start = text.render("Start Game", True, black)
The_Screen.screen.blit(game_start, align(game_start))
pygame.display.flip

#Main Menu
b = 0
while choosing:
	clock.tick(10)

	event_move = pygame.event.get(pygame.MOUSEMOTION)
	event_click = pygame.event.get(pygame.MOUSEBUTTONDOWN)
	if len(pygame.event.get(pygame.QUIT)) >= 1:
		pygame.quit()
		choosing = False
		playing = False

	#This tests to see if an event is returned
	try:
		blah = event_move[0]
		is_event = True
	except IndexError:
		is_event = False
	if is_event:
		#Now that an event is determined to exist check to see if the mouse in hovering over the box
		x_temp, y_temp = event_move[0].dict["pos"]
		if start_button.collidepoint(x_temp, y_temp):
			The_Screen.screen.fill(brown, start_button)
		pygame.draw.rect(The_Screen.screen, black, start_button, 3)
		game_start = text.render("Start Game", True, black)
		The_Screen.screen.blit(game_start, align(game_start))
		pygame.display.flip()
		The_Screen.screen.fill(darkgreen)

	if len(event_click) >= 1:
		for i in event_click:
			if i.dict["button"] == 1:
				x_temp, y_temp = i.dict["pos"]
				if start_button.collidepoint(x_temp, y_temp):
					choosing = False

pygame.event.clear()


The_Deck.deal(4)
#Display the inital setup
The_Screen.display()
pygame.display.flip()




#Start the Main Loop
while playing:
	clock.tick(10)
	
	#Check for exiting the screen
	ev_list = pygame.event.get()
	for ev in ev_list:
		if ev.type == pygame.QUIT:
			pygame.quit()
			break

		if ev.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = ev.dict["pos"]
			The_Deck.hover(mouse_pos)
			The_Screen.display()
			pygame.display.flip()			
	
		if ev.type == pygame.KEYDOWN:
			if value(ev) == "return":
				played = The_Deck.play()
				The_Rules.is_valid(played)
				The_Screen.display()


		#if The_Rules.turn == 2:
			






#			if ev.key == pygame.a:
#			pygame.key.name(ev.key) This returns the string value of the key pressed

			








