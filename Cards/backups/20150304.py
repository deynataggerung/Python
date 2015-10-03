import pygame
import copy
from random import randint
#Before I switched the cards to pop up on mouse hover. It's only on click after



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
		self.position = (0,0)
		self.hitbox = pygame.Rect(0,0,20,20)
	
	#Function to display image to screen

	#
	def update_pos(self, coord):
		try:
			self.position = coord
			x, y = self.position
			self.hitbox = pygame.Rect(self.position, (x+self.image.get_width()*0.2, y+self.image.get_height()))
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
		self.cards["back"] = Card(
		#A list of the keys for easy referencing of the deck
		self.reference = self.cards.keys()
		self.final_hover = False
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
		self.hands = [self.rearrange(self.reference[0:self.hand_size]), self.rearrange(self.reference[self.hand_size:self.hand_size*2]), self.rearrange(self.reference[self.hand_size*2:self.hand_size*3]), self.rearrange(self.reference[self.hand_size*3:])]

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
		return arranged

	def display_hand(self, hand_num = 1):
		screen.fill(darkgreen)
		hiq = self.hands[hand_num-1]

		print "hiq", hiq
		print
		#Don't screw up on uno
		num = len(hiq)
		if num == 1:
			screen.blit(self.cards[hiq[0]].image(), align(self.cards[hiq[0]].image(), "bottom", "center"))
		else:
			#Even hands have an imaginary pivot card which the other cards are based off of
			if num %2 == 0:
				first_half = hiq[0: num/2-1]
				second_half = hiq[num/2+2:]
				pivot = pygame.Rect(align(self.cards[hiq[0]].image, "bottom", "center"), (168,243))
				pivot_coord = (pivot.x, pivot.y)

				lpivot = hiq[num/2]
				lpivot_coord = offset(pivot, -0.1, "horizontal", pivot.coord)
				rpivot = hiq[num/2+1]
				rpivot_coord =  offset(pivot, 0.1, "horizontal", pivot.coord)

				ldistance = num*-0.2-0.1
				rdistance = 0.1
			elif num%2 == 1:
				first_half = hiq[0: num/2]
				second_half = hiq[num/2:]
				print hiq[num/2+1]
				pivot = self.cards[hiq[num/2+1]].image
				pivot_coord = align(self.cards[hiq[num/2]].image, "bottom", "center")

				lpivot = pivot
				lpivot_coord = pivot_coord
				rpivot = pivot
				rpivot_coord = pivot_coord

				ldistance = (num/2)*-0.2
				rdistance = 0
		
			for i in range(len(first_half)):
				the_coordinates = offset(pivot, ldistance+i*0.2, "horizontal", pivot_coord)

				if self.cards[first_half[i]].identifier == self.final_hover:
					the_coordinates = offset(pivot, 0.4, "vertical", the_coordinates)

				screen.blit(self.cards[first_half[i]].image, the_coordinates)
				#Updates the position of the card to match
				self.cards[first_half[i]].update_pos(the_coordinates)

			screen.blit(lpivot, lpivot_coord)
			screen.blit(rpivot, rpivot_coord)
			for i in range(len(second_half)):
				the_coordinates = offset(pivot, rdistance+i*0.2, "horizontal", pivot_coord)

				#Checks to see if there is a hover on a card and raises that card
				if self.cards[second_half[i]].identifier == self.final_hover:
					the_coordinates = offset(pivot, 0.4, "vertical", the_coordinates)

				screen.blit(self.cards[second_half[i]].image, the_coordinates)
				self.cards[second_half[i]].update_pos(the_coordinates)

	#Tests to see if the mouse is hovering over a card
	def hover(self, coord):
		check = self.hands[0]
		self.final_hover = False
		for n in check:
			#Card in question
			ciq = self.cards[n]
			if ciq.hitbox.collidepoint(coord):
				self.final_hover = ciq.identifier
		return self.final_hover

#	def play(self):
		


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
	


#Create the Deck
The_Deck = Deck()

#It's important to start sometime
pygame.init()

#Defining colors for screen
black = (0,0,0)
white = (255,255,255)
green = (0,255,255)
darkgreen = (10,104,0)
brown = (127, 55, 0)

#Create Screen
screen = pygame.display.set_mode((1000,800))

#Fonts
text = pygame.font.Font("unrealised.ttf", 120)

#Conditions for Starting
choosing = True
playing = True
hand = 1

clock = pygame.time.Clock()
start_button = pygame.Rect(align((500,200)), (500,200))

screen.fill(darkgreen)
pygame.draw.rect(screen, black, start_button, 3)
game_start = text.render("Start Game", True, black)
screen.blit(game_start, align(game_start))
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
			screen.fill(brown, start_button)
		pygame.draw.rect(screen, black, start_button, 3)
		game_start = text.render("Start Game", True, black)
		screen.blit(game_start, align(game_start))
		pygame.display.flip()
		screen.fill(darkgreen)

	if len(event_click) >= 1:
		for i in event_click:
			if i.dict["button"] == 1:
				x_temp, y_temp = i.dict["pos"]
				if start_button.collidepoint(x_temp, y_temp):
					choosing = False

pygame.event.clear()

The_Deck.deal(4)
#Display the inital setup
The_Deck.display_hand()


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
			print 			
	
		if ev.type == pygame.MOUSEMOTION:
			mouse_pos = ev.dict["pos"]
			The_Deck.hover(mouse_pos)
			The_Deck.display_hand()
			pygame.display.flip()

			








