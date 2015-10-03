import os
import pygame, sys
from pygame.locals import *

#Remember that all x inputs must be the actual spot of that piece, not the piece number. These may sometimes coincide


class Pawn(object): 
	def __init__(self, x, me, color): # x is the horizontal position of the piece, me is the identity of the piece(each piece has a number
		if color == "black":
			self.display = pygame.image.load('bpawn.png').convert_alpha() #display contains the png image of the piece
			y = 2
		elif color == "white":
			self.display = pygame.image.load('wpawn.png').convert_alpha()
			y = 7
		else:
			return False
		self.position = [me, y]
		self.identity = "Pawn%s" % me
		self.color = color

	def show(self):
		if self.color == 'black':
			screen.blit(self.display, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))
		elif self.color == 'white':
			screen.blit(self.display, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))


class Rook(object):
	def __init__(self, x, me, color):
		if color == "black":
			self.display = "|bR "
			y = 1
		elif color == "white":
			self.display = "|bR "
			y = 8
		else:
			return False
		self.position = [x,y]
		self.identity = "Rook%s" % me
		self.color = color
		
	def show(self):
		if self.color == 'black':
			screen.blit(brookimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*100 + 2.5))
		elif self.color == 'white':
			screen.blit(wrookimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*100 + 2.5))



class Knight(object):
	def __init__(self, x, me, color):
		if color == "black":
			self.display = "|bk "
			y = 1
		elif color == "white":
			self.display = "|wk "
			y = 8
		else:
			return False
		self.position = [x, y]
		self.identity = "Knight%s" % me
		self.color = color

	def show(self):
		if self.color == 'black':
			screen.blit(bknightimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))
		elif self.color == 'white':
			screen.blit(wknightimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))

class Bishop(object):
	def __init__(self, x, me, color):
		if color == "black":
			self.display = "|bB "
			y = 1
		elif color == "white":
			self.display = "|wB "
			y = 8
		else:
			return False
		self.position = [x, y]
		self.identity = "Bishop%s" % me
		self.color = color

	def show(self):
		if self.color == 'black':
			screen.blit(bbishopimg, ((self.position[0]-1)*50 +2.5, (self.position[1]-1)*50 + 2.5))
		elif self.color == 'white':
			screen.blit(wbishopimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))



class King(object):
	def __init__(self, color):
		if color == "black":
			self.display = "|bK "
			y = 1
		elif color == "white":
			self.display = "|bK "
			y = 8
		else:
			return False
		self.position = [4, y]
		self.identity = "King"
		self.color = color

	def show(self):
		if self.color == 'black':
			screen.blit(bkingimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))
		elif self.color == 'white':
			screen.blit(wkingimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))


class Queen(object):
	def __init__(self, color):
		if color == "black":
			self.display = "|bQ "
			y = 1
		elif color =="white":
			self.display = "|wQ "
			y = 8
		else:
			return False
		self.position = [5,y]
		self.identity = "Queen"
		self.color = color

	def show(self):
		if self.color == 'black':
			screen.blit(bqueenimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))
		elif self.color == 'white':
			screen.blit(wqueenimg, ((self.position[0]-1)*50 + 2.5, (self.position[1]-1)*50 + 2.5))


temp = []
black = {}
white = {}
for f in range(1,9):
	temp.append(Pawn(f, f, "black"))
for f in temp:
	black[f.identity] = f
rooktemp = Rook(1, 1, "black")
black[rooktemp.identity] = rooktemp
rooktemp = Rook(8, 2, "black")
black[rooktemp.identity] = rooktemp
knighttemp = Knight(2, 1, "black")
black[knighttemp.identity] = knighttemp
knighttemp = Knight(7, 2, "black")
black[knighttemp.identity] = knighttemp
bishtemp = Bishop(3, 1, "black")
black[bishtemp.identity] = bishtemp
bishtemp = Bishop(6, 2, "black")
black[bishtemp.identity] = bishtemp
kingtemp = King("black")
black[kingtemp.identity] = kingtemp
queentemp = Queen("black")
black[queentemp.identity] = queentemp



temp = []
for f in range(1,9):
	temp.append(Pawn(f, f, "white"))
for f in temp:
	white[f.identity] = f
rooktemp = Rook(1, 1, "white")
white[rooktemp.identity] = rooktemp
rooktemp = Rook(8, 2, "white")
white[rooktemp.identity] = rooktemp
knighttemp = Knight(2, 1, "white")
white[knighttemp.identity] = knighttemp
knighttemp = Knight(7, 2, "white")
white[knighttemp.identity] = knighttemp
bishtemp = Bishop(3, 1, "white")
white[bishtemp.identity] = bishtemp
bishtemp = Bishop(6, 2, "white")
white[bishtemp.identity] = bishtemp
kingtemp = King("white")
white[kingtemp.identity] = kingtemp
queentemp = Queen("white")
white[queentemp.identity] = queentemp




pygame.init()
screen = pygame.display.set_mode((405,405))

wknightimg = pygame.image.load('wknight.png').convert_alpha()
wkingimg = pygame.image.load('wking.png').convert_alpha()
wbishopimg = pygame.image.load('wbishop.png').convert_alpha()
wpawnimg = pygame.image.load('wpawn.png').convert_alpha()
wqueenimg = pygame.image.load('wqueen.png').convert_alpha()
wrookimg = pygame.image.load('wrook.png').convert_alpha()

bknightimg = pygame.image.load('bknight.png').convert_alpha()
bkingimg = pygame.image.load('bking.png').convert_alpha()
bbishopimg = pygame.image.load('bbishop.png').convert_alpha()
bpawnimg = pygame.image.load('bpawn.png').convert_alpha()
bqueenimg = pygame.image.load('bqueen.png').convert_alpha()
brookimg = pygame.image.load('brook.png').convert_alpha()

background = pygame.image.load('Chess_Board.png').convert()

screen.blit(background, (0,0))
pygame.display.update()
raw_input()
for f in black:
	black[f].show()
	white[f].show()

pygame.display.update()
raw_input()






