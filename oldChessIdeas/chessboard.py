import pygame, sys
from pygame.locals import *

pygame.init()
class GameObject:
	def __init__(self, image, height, speed):
		self.image = image
		self.pos = image.get_rect().move(height, height)
	def move(self):
		self.pos = self.pos.move(100, 100)

screen = pygame.display.set_mode((810,810))
player = pygame.image.load('knight.png').convert_alpha()
background = pygame.image.load('Chess_Board.png').convert()
screen.blit(background, (0,0))
objects = []
o = GameObject(player, 5, 1)

while 1:
	for event in pygame.event.get():
		if event.type == QUIT:
			sys.exit()
		if event.type == KEYDOWN:
			screen.blit(background, o.pos, o.pos)
			o.move()
			screen.blit(o.image, o.pos)
		if event.type == KEYDOWN:
			screen.blit(background, o.pos, pos)
			o.move()
			o.move()
			screen.blit(olimage, o.pos)
	#for o in objects:
		#screen.blit(background, o.pos, o.pos)
	#for o in objects:
		#o.move()
		#screen.blit(o.image, o.pos)
	pygame.display.update()
	pygame.time.delay(100)



class Board(object):
	def __init__(self, b, w):
		self.pieces = [b, w]
		self.piecesact = self.pieces
		self.translator = {1:2, 2:4, 3:6, 4:8, 5:10, 6:12, 7:14, 8:16}
		for i in self.piecesact[0]:
			self.piecesact[0][i].position[1] = self.translator[self.piecesact[0][i].position[1]]
		for i in self.piecesact[1]:
			self.piecesact[1][i].position[1] = self.translator[self.piecesact[1][i].position[1]]
			

		self.display = [[' ', '| 1 ', '| 2 ', '| 3 ', '| 4 ', '| 5 ', '| 6 ', '| 7 ', '| 8 ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['1', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['2', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['3', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['4', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['5', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['6', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['7', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['8', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|']]
		for i in range(2):
			for l in self.pieces[i]:
				self.display[self.piecesact[i][l].position[1]][self.piecesact[i][l].position[0]] = self.pieces[i][l].display

	def playermove(self):
		print ""

	def show(self):
		os.system("cls")
		for i in self.display:
			print " ".join(i)
