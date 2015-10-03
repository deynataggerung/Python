import pygame

#Next I'm looking to work on adding an event listener for a click. If the person clicks, it will check the place clicked for possible moves and display that.


#allow for possible size shifts
spot = 100
boardSize = 800

class Piece(object):
	def __init__(self): #blank init to give default values in case of failure
		self.x = -1
		self.y = -1
		self.identity = "basic"

	def show(self): # shows the piece on the screen
		screen.blit(self.display, (self.position[0]*spot, self.position[1]*spot))

	# add defs checking horizontally, diagonally, specific spot to be called by each individual type of piece depending on how they work.

class Pawn(Piece):
	def __init__(self, me, color):
		if color == "black":
			self.display = pygame.image.load('images\\bPawn.png').convert_alpha()
			self.y = 1
		if color == "white":
			self.display = pygame.image.load('images\\wPawn.png').convert_alpha()
			self.y = 6
		
		self.x = me
		self.position = [self.x, self.y]
		self.identity = color[0] + "Pawn%s" % me
		self.color = color
		self.value = 1
		
class Bishop(Piece):
	def __init__(self, me, color):
		if color == "black": # loads in the correct image for chosen piece
			self.display = pygame.image.load('images\\bBishop.png').convert_alpha()
			self.y = 0
		if color == "white":
			self.display = pygame.image.load('images\\wBishop.png').convert_alpha()
			self.y = 7

		if me == 0: # decides where the initial placement of the piece will be
			self.x = 2
		elif me == 1:
			self.x = 5
		else:
			self.x = -1

		self.position = [self.x, self.y]
		self.identity = color[0] + "Bishop%s" % me
		self.color = color
		self.value = 3

class Knight(Piece):
	def __init__(self, me, color):
		if color == "black":
			self.display = pygame.image.load('images\\bKnight.png').convert_alpha()
			self.y = 0
		elif color == "white":
			self.display = pygame.image.load('images\\wKnight.png').convert_alpha()
			self.y = 7

		if me == 0:
			self.x = 1
		elif me == 1:
			self.x = 6

		self.position = [self.x, self.y]
		self.identity = color[0] + "Knight%s" % me
		self.color = color
		self.value = 3
	
class Rook(Piece):
	def __init__(self, me, color):
		if color == "black":
			self.display = pygame.image.load('images\\bRook.png').convert_alpha()
			self.y = 0
		elif color == "white":
			self.display = pygame.image.load('images\\wRook.png').convert_alpha()
			self.y = 7

		if me == 0:
			self.x = 0
		elif me == 1:
			self.x = 7

		self.position = [self.x, self.y]
		self.identity = color[0] + "Rook%s" % me
		self.color = color
		self.value = 5

class Queen(Piece):
	def __init__(self, color):
		if color == "black":
			self.display = pygame.image.load('images\\bQueen.png').convert_alpha()
			self.y = 0
		elif color == "white":
			self.display = pygame.image.load('images\\wQueen.png').convert_alpha()
			self.y = 7

		self.x = 3
		self.position = [self.x, self.y]
		self.identity = color[0] + "Queen"
		self.color = color
		self.value = 7

class King(Piece):
	def __init__(self, color):
		if color == "black":
			self.display = pygame.image.load('images\\bKing.png').convert_alpha()
			self.y = 0
		elif color == "white":
			self.display = pygame.image.load('images\\wKing.png').convert_alpha()
			self.y = 7

		self.x = 4
		self.position = [self.x, self.y]
		self.identity = color[0] + "King"
		self.color = color
		self.value = 10

class Board(object):
	def __init__(self):
		self.spaces = [["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""]]
	
	def refresh(self):
		for i in bPieces.keys():
			self.spaces[bPieces[i].y][bPieces[i].x] = bPieces[i]
		for i in wPieces.keys():
			self.spaces[wPieces[i].y][wPieces[i].x] = wPieces[i]
		for i in self.spaces:
			print i

		for i in wPieces.keys():
			wPieces[i].show()
		for i in bPieces.keys():
			bPieces[i].show()

		pygame.display.flip()
		

def resize(orig, magnitude):
	x_comp, y_comp = orig.get_size()
	x_comp = int(x_comp*magnitude)
	y_comp = int(y_comp*magnitude)
	return pygame.transform.scale(orig, (x_comp, y_comp))
#Starting of the pygame portion

pygame.init()

#Conditions for Starting
screen = pygame.display.set_mode((boardSize, boardSize))

#display board
board = pygame.image.load("images\\brownChessBoard.png")
screen.blit(board, (0,0))
pygame.display.flip()

#initialize the pieces
wPieces = {}
bPieces = {}
for i in range(8):
	temp = Pawn(i, "white")
	wPieces[temp.identity] = temp
	temp = Pawn(i, "black")
	bPieces[temp.identity] = temp

for i in range(2):
	temp = Bishop(i, "white")
	wPieces[temp.identity] = temp
	temp = Bishop(i, "black")
	bPieces[temp.identity] = temp

	temp = Knight(i, "white")
	wPieces[temp.identity] = temp
	temp = Knight(i, "black")
	bPieces[temp.identity] = temp

	temp = Rook(i, "white")
	wPieces[temp.identity] = temp
	temp = Rook(i, "black")
	bPieces[temp.identity] = temp

temp = Queen("white")
wPieces[temp.identity] = temp
temp = Queen("black")
bPieces[temp.identity] = temp

temp = King("white")
wPieces[temp.identity] = temp
temp = King("black")
bPieces[temp.identity] = temp

mainBoard = Board()
mainBoard.refresh()


clock = pygame.time.Clock()
playtime = 0.0


while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break;

	

