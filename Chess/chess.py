import pygame
from copy import deepcopy
import random

#ToDo: Bot that trash talks :P

#allow for possible size shifts
SPOT = 100
boardSize = 800

class Piece(object):
	def __init__(self): #blank init to give default values in case of failure
		self.x = -1
		self.y = -1
		self.identity = "basic"
		self.moveCount = 0

	def show(self): # shows the piece on the screen
		screen.blit(self.display, (self.position[0]*SPOT, self.position[1]*SPOT))

	def checkDiagonal(self, myBoard): #position comes in as 0-7 values goes out the same way
		x, y = self.position
		moves = []
		c = 1
		searching = True
		
		while(searching): # Checks up and right
			if myBoard.hasPiece((x + c, y - c)) == None:
				break
			if myBoard.hasPiece((x + c, y - c)): # if there is a piece in the spot being checked, end searching
				if myBoard.spaces[y-c][x+c].color != myBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x + c), (y - c)))
				searching = False
			else:
				moves.append(((x + c), (y - c)))
				c += 1

		c = 1 #Important to reset my counters
		searching = True
		while(searching): # Checks up and left
			if myBoard.hasPiece((x - c, y - c)) == None:
				break
			if myBoard.hasPiece((x - c, y - c)): # if there is a piece in the spot being checked, end searching
				if myBoard.spaces[y-c][x-c].color != myBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x - c), (y - c)))
				searching = False
			else:
				moves.append(((x - c), (y - c)))
				c += 1

		c = 1
		searching = True
		while(searching): # Checks down and right
			if myBoard.hasPiece((x + c, y + c)) == None:
				break
			if myBoard.hasPiece((x + c, y + c)): # if there is a piece in the spot being checked, end searching
				if myBoard.spaces[y+c][x+c].color != myBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x + c), (y + c)))
				searching = False
			else:
				moves.append(((x + c), (y + c)))
				c += 1

		c = 1
		searching = True
		while(searching): # Checks down and left
			if myBoard.hasPiece((x - c, y + c)) == None:
				break
			if myBoard.hasPiece((x - c, y + c)): # if there is a piece in the spot being checked, end searching
				if myBoard.spaces[y+c][x-c].color != myBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x - c), (y + c)))
				searching = False
			else:
				moves.append(((x - c), (y + c)))
				c += 1
		return moves

	def checkHorizontal(self, myBoard):
		x, y = self.position
		searching = True
		moves = []
		reverse = 1
		xDir = 1
		yDir = 0
		xc = 1 * xDir * reverse
		yc = 1 * yDir * reverse
		c = 0
		stopInf = 0
		
		while searching:
			if myBoard.hasPiece((x+xc, y+yc)) == None:
				if yDir == 1:
					reverse *= -1
				temp = yDir
				yDir = xDir
				xDir = temp
				xc = 1 * xDir * reverse
				yc = 1 * yDir * reverse
				c = 0
				continue
			if myBoard.hasPiece((x+xc, y+yc)):
				if myBoard.spaces[y+yc][x+xc].color != myBoard.spaces[y][x].color:
					moves.append((x+xc, y+yc))
				if yDir == 1:
					reverse *= -1
				temp = yDir
				yDir = xDir
				xDir = temp
				c = 0
			else:
				moves.append((x+xc, y+yc))
				c += 1
			xc = (1+c) * xDir * reverse
			yc = (1+c) * yDir * reverse

			stopInf += 1
			if stopInf > 20:
				searching = False
			if ((x+xc, y+yc) in moves):
				searching = False

		return moves
		

	def move(self, position, myBoard):
		x, y = position
		if myBoard.hasPiece(position):
			takenPiece = myBoard.spaces[y][x].identity
			global playingGame
			global winner
			if takenPiece == "wKing":
				playingGame = False
				winner = "BLACK"
			elif takenPiece == "bKing":
				playingGame = False
				winner = "WHITE"
			if takenPiece in wPieces: del wPieces[takenPiece]
			if takenPiece in bPieces: del bPieces[takenPiece]
		self.position = [x,y]
		self.moveCount += 1

		

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
		self.moveCount = 0

	def moves(self, myBoard):
		x, y = self.position
		moves = []
		#Determine which side is being picked, I may have to remove this later
		if self.color == "black":
			modifier = 1
		else:
			modifier = -1

		# Check for a simple forward movement
		if not myBoard.hasPiece((x, y + modifier)):
			moves.append((x, y + modifier))
			#check for double space on first move.
			if self.moveCount == 0 and not myBoard.hasPiece((x, y + 2 * modifier)):
				moves.append((x, y + 2 * modifier))
		
		# Testing to see if there are pieces at a diagonal to take
		if myBoard.hasPiece(((x + 1), (y + modifier))):
			if myBoard.spaces[y + modifier][x + 1].color != myBoard.spaces[y][x].color:
				moves.append((x + 1, y + modifier))
		if myBoard.hasPiece((x - 1, y + modifier)):
			if myBoard.spaces[y + modifier][x - 1].color != myBoard.spaces[y][x].color:
				moves.append((x - 1, y + modifier))

		return moves
			
		
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
		self.moveCount = 0

	def moves(self, myBoard):
		return self.checkDiagonal(myBoard)
		

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
		self.moveCount = 0

	def moves(self, myBoard):
		x, y = self.position
		distances1 = [1,-1] 
		distances2 = [2, -2]
		moves = []
		for i in distances1:
			for j in distances2:
				if myBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if myBoard.hasPiece((x+i, y+j)):
					if myBoard.spaces[y+j][x+i].color != myBoard.spaces[y][x].color:
						moves.append((x+i,y+j))
					else:
						continue
				else:
					moves.append((x+i, y+j))

		for j in distances1: # Can't think of a good way to do this once without random overlap
			for i in distances2:
				if myBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if myBoard.hasPiece((x+i, y+j)):
					if myBoard.spaces[y+j][x+i].color != myBoard.spaces[y][x].color:
						moves.append((x+i, y+j))
					else:
						continue;
				else:
					moves.append((x+i, y+j))
		return moves
				
	
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
		self.moveCount = 0
	
	def moves(self, myBoard):
		return self.checkHorizontal(myBoard)

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
		self.moveCount = 0

	def moves(self, myBoard):
		moves = []
		for i in self.checkHorizontal(myBoard):
			moves.append(i)
		for i in self.checkDiagonal(myBoard):
			moves.append(i)
		return moves

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
		self.moveCount = 0

		
	def moves(self, myBoard):
		moves = []
		x, y = self.position
		for i in [-1,0,1]:
			for j in [-1,0,1]: #Same as Knight method but with only one space
				if myBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if myBoard.hasPiece((x+i, y+j)):
					if myBoard.spaces[y+j][x+i].color != myBoard.spaces[y][x].color:
						moves.append((x+i, y+j))
				else:
					moves.append((x+i, y+j))
		return moves

class Board(object):
	def __init__(self):
		self.spaces = [["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""]]
		self.tone = pygame.image.load('images\\move.png').convert_alpha()
	
	def refresh(self, anybPieces, anywPieces, actual=True):
		for i in range(8):
			for j in range(8):
				self.spaces[i][j] = ""
		for i in anybPieces.keys():
			self.spaces[anybPieces[i].position[1]][anybPieces[i].position[0]] = anybPieces[i]
		for i in anywPieces.keys():
			self.spaces[anywPieces[i].position[1]][anywPieces[i].position[0]] = anywPieces[i]

		screen.blit(board, (0,0))

		if actual:
			screen.blit(self.tone, tuple([x*SPOT for x in selectedPiece]))

			for i in possibleMoves:
				# right here add a conversion from 0-7 values into 0-700 values
				screen.blit(self.tone, tuple([x*SPOT for x in i]))

			for i in anywPieces.keys():
				wPieces[i].show()
			for i in anybPieces.keys():
				bPieces[i].show()

			pygame.display.flip()

	def hasPiece(self, position):
		x, y = position
		if x < 0 or y < 0:
			return None
		try:
			if self.spaces[y][x] != "":
				return True
			else:
				return False
		except IndexError:
			return None
		
def consequences(thisMove, myBoard, bPiece, wPiece, c):
	myBoard.refresh(bPiece, wPiece, False)
	myBoard.spaces[thisMove.mFrom[1]][thisMove.mFrom[0]].move(thisMove.mTo, myBoard)
	myBoard.refresh(bPiece, wPiece, False)
	if c % 2 == 0:
		allMoves = findPossibleMoves(wPiece, myBoard)
	else:
		allMoves = findPossibleMoves(bPiece, myBoard)
	if c == 1:
		return thisMove.gain;
	c += 1;
	net = 0
	for i in allMoves:
		net += consequences(i, deepcopy(myBoard), deepcopy(bPiece), deepcopy(wPiece), c)
	return thisMove.gain + net;

def calculateMove():
	iBoard = Board()
	iBoard.refresh(bPieces, wPieces)
	firstMoves = findPossibleMoves(bPieces, iBoard)
	for i in firstMoves:
		i.net = consequences(i, Board(), deepcopy(bPieces), deepcopy(wPieces), 0)
		print i.mTo
		print i.gain
		print i.net
		print

	bestMove = firstMoves[random.randint(0, len(firstMoves) - 1)]
	highest = 0
	for i in firstMoves:
		if i.net > highest:
			highest = i.gain
			bestMove = i
	return bestMove


	
	
class Move(object):
	def __init__(self, board, mFrom, mTo):
		self.mTo = mTo
		self.mFrom = mFrom
		if board.spaces[mTo[1]][mTo[0]] == "":
			self.take = False
			self.gain = 0
		else:
			self.take = True
			self.gain = board.spaces[mTo[1]][mTo[0]].value
		self.net = self.gain

	def addValue(worth):
		if worth > 0:
			self.gain += worth;
		else:
			self.loss += worth;
		
	

def findPossibleMoves(pieces, board):
	totalMoves = []
	for i in pieces.keys():
		for f in pieces[i].moves(board):
			totalMoves.append(Move(board, pieces[i].position, f))
	return totalMoves
	

def resize(orig, magnitude):
	x_comp, y_comp = orig.get_size()
	x_comp = int(x_comp*magnitude)
	y_comp = int(y_comp*magnitude)
	return pygame.transform.scale(orig, (x_comp, y_comp))


#Starting of the pygame portion

pygame.init()

#Inital Variables
playingGame = True
screen = pygame.display.set_mode((boardSize, boardSize))
selectedPiece = (9,9)
possibleMoves = []
possibleTakes = []
turn = "white"

#Add Font/Color
end = pygame.font.SysFont("Times", 100)
black = (0,0,0)
red = (255,0,0)

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
mainBoard.refresh(bPieces, wPieces)
for i in mainBoard.spaces:
	print i

# variables

clock = pygame.time.Clock()
playtime = 0.0


while playingGame:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break;
	if ev.type == pygame.MOUSEBUTTONDOWN:
		x, y = ev.pos #0-700
		x /= SPOT
		y /= SPOT  # 0-7
		position = 	((x), (y))

		if position == selectedPiece: # If you're clicking twice, unselect
			possibleMoves = []
			selectedPiece = (9, 9) 

		elif position in possibleMoves: # If you want to move a piece
			mainBoard.spaces[selectedPiece[1]][selectedPiece[0]].move(position, mainBoard)  #access the board and the piece that has been selected. Then update that piece's position
			turn = "black" # pass off the move to black
			possibleMoves = [] #clear
			selectedPiece = (9, 9)

		else:
			try:
				testPiece = mainBoard.spaces[y][x]
				possibleMoves = []
				if mainBoard.spaces[y][x].color == turn:
					for i in mainBoard.spaces[y][x].moves(mainBoard):
						possibleMoves.append(i)
				selectedPiece = position
				
			except AttributeError:
				print "Attribute Error"

		mainBoard.refresh(bPieces, wPieces)

	if turn == "black":
		bMove = calculateMove()
		mainBoard.spaces[bMove.mFrom[1]][bMove.mFrom[0]].move(bMove.mTo, mainBoard)
		mainBoard.refresh(bPieces, wPieces)
		turn = "white"

finale = end.render("%s WINS!" % winner, True, red)
screen.blit(finale, (90, 350))
pygame.display.flip()

while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break;

