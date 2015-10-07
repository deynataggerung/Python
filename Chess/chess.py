import pygame


#allow for possible size shifts
SPOT = 100
boardSize = 800

class Piece(object):
	def __init__(self): #blank init to give default values in case of failure
		self.x = -1
		self.y = -1
		self.identity = "basic"

	def show(self): # shows the piece on the screen
		screen.blit(self.display, (self.position[0]*SPOT, self.position[1]*SPOT))

	def checkDiagonal(self, position): #position comes in as 0-7 values goes out the same way
		moves = []
		x, y = position
		c = 1
		searching = True
		
		while(searching): # Checks up and right
			if mainBoard.hasPiece((x + c, y - c)) == None:
				break
			if mainBoard.hasPiece((x + c, y - c)): # if there is a piece in the spot being checked, end searching
				if mainBoard.spaces[y-c][x+c].color != mainBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x + c), (y - c)))
				searching = False
			else:
				moves.append(((x + c), (y - c)))
				c += 1

		c = 1 #Important to reset my counters
		searching = True
		while(searching): # Checks up and left
			if mainBoard.hasPiece((x - c, y - c)) == None:
				break
			if mainBoard.hasPiece((x - c, y - c)): # if there is a piece in the spot being checked, end searching
				if mainBoard.spaces[y-c][x-c].color != mainBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x - c), (y - c)))
				searching = False
			else:
				moves.append(((x - c), (y - c)))
				c += 1

		c = 1
		searching = True
		while(searching): # Checks down and right
			if mainBoard.hasPiece((x + c, y + c)) == None:
				break
			if mainBoard.hasPiece((x + c, y + c)): # if there is a piece in the spot being checked, end searching
				if mainBoard.spaces[y+c][x+c].color != mainBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x + c), (y + c)))
				searching = False
			else:
				moves.append(((x + c), (y + c)))
				c += 1

		c = 1
		searching = True
		while(searching): # Checks down and left
			if mainBoard.hasPiece((x - c, y + c)) == None:
				break
			if mainBoard.hasPiece((x - c, y + c)): # if there is a piece in the spot being checked, end searching
				if mainBoard.spaces[y+c][x-c].color != mainBoard.spaces[y][x].color: # allow taking opponents
					moves.append(((x - c), (y + c)))
				searching = False
			else:
				moves.append(((x - c), (y + c)))
				c += 1
		return moves

	def checkHorizontal(self, position):
		searching = True
		x, y = position
		moves = []
		reverse = 1
		xDir = 1
		yDir = 0
		xc = 1 * xDir * reverse
		yc = 1 * yDir * reverse
		c = 0
		stopInf = 0
		
		while searching:
			print "(%d + %d, %d + %d)" % (x, xc, y, yc)
			if mainBoard.hasPiece((x+xc, y+yc)) == None:
				if yDir == 1:
					reverse *= -1
				temp = yDir
				yDir = xDir
				xDir = temp
				xc = 1 * xDir * reverse
				yc = 1 * yDir * reverse
				c = 0
				continue
			if mainBoard.hasPiece((x+xc, y+yc)):
				if mainBoard.spaces[y+yc][x+xc].color != mainBoard.spaces[y][x].color:
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
		

	def move(self, position):
		x, y = position
		if mainBoard.hasPiece(position):
			takenPiece = mainBoard.spaces[y][x].identity
			global playingGame
			global winner
			if takenPiece == "wKing":
				playingGame = False
				winner = "WHITE"
			elif takenPiece == "bKing":
				playingGame = False
				winner = "BLACK"
			if takenPiece in wPieces: del wPieces[takenPiece]
			if takenPiece in bPieces: del bPieces[takenPiece]
		self.position = [x,y]

		

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

	def moves(self, position):
		x, y = position
		print position
		moves = []
		#Determine which side is being picked, I may have to remove this later
		if mainBoard.spaces[y][x].color == "black":
			modifier = 1
		else:
			modifier = -1

		# Check for a simple forward movement
		if not mainBoard.hasPiece((x, y + modifier)):
			moves.append((x, y + modifier))

		# Allow double space on first move
		if modifier == 1 and y == 1:
			moves.append((x, y + 2 * modifier))
		if modifier == -1 and y == 6:
			moves.append((x, y + 2 * modifier))
		
		# Testing to see if there are pieces at a diagonal to take
		if mainBoard.hasPiece(((x + 1), (y + modifier))):
			if mainBoard.spaces[y + modifier][x + 1].color != mainBoard.spaces[y][x].color:
				moves.append((x + 1, y + modifier))
		if mainBoard.hasPiece((x - 1, y + modifier)):
			if mainBoard.spaces[y + modifier][x - 1].color != mainBoard.spaces[y][x].color:
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

	def moves(self, position):
		return self.checkDiagonal(position)
		

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

	def moves(self, position):
		x, y = position
		distances1 = [1,-1] 
		distances2 = [2, -2]
		moves = []
		for i in distances1:
			for j in distances2:
				if mainBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if mainBoard.hasPiece((x+i, y+j)):
					if mainBoard.spaces[y+j][x+i].color != mainBoard.spaces[y][x].color:
						moves.append((x+i,y+j))
				else:
					moves.append((x+i, y+j))

		distances1 = [2,-2]
		distances2 = [1, -1]
		for i in distances1: # Can't think of a good way to do this once without random overlap
			for j in distances2:
				if mainBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if mainBoard.hasPiece((x+i, y+j)):
					if mainBoard.spaces[y+j][x+i].color != mainBoard.spaces[y][x].color:
						moves.append((x+i, y+j))
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
	
	def moves(self, position):
		return self.checkHorizontal(position)

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

	def moves(self, position):
		moves = []
		for i in self.checkHorizontal(position):
			moves.append(i)
		for i in self.checkDiagonal(position):
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

		
	def moves(self, position):
		moves = []
		for i in [-1,0,1]:
			for j in [-1,0,1]: #Same as Knight method but with only one space
				if mainBoard.hasPiece((x+i, y+j)) == None or (x+i, y+j) in moves:
					continue
				if mainBoard.hasPiece((x+i, y+j)):
					if mainBoard.spaces[y+j][x+i].color != mainBoard.spaces[y][x].color:
						moves.append((x+i, y+j))
				else:
					moves.append((x+i, y+j))
		return moves

class Board(object):
	def __init__(self):
		self.spaces = [["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""], ["","","","","","","",""]]
		self.tone = pygame.image.load('images\\move.png').convert_alpha()
	
	def refresh(self):
		for i in range(8):
			for j in range(8):
				self.spaces[i][j] = ""
		for i in bPieces.keys():
			self.spaces[bPieces[i].position[1]][bPieces[i].position[0]] = bPieces[i]
		for i in wPieces.keys():
			self.spaces[wPieces[i].position[1]][wPieces[i].position[0]] = wPieces[i]

		screen.blit(board, (0,0))


		screen.blit(self.tone, tuple([x*SPOT for x in selectedPiece]))
		for i in possibleMoves:
			# right here add a conversion from 0-7 values into 0-700 values
			screen.blit(self.tone, tuple([x*SPOT for x in i]))

		for i in wPieces.keys():
			wPieces[i].show()
		for i in bPieces.keys():
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
mainBoard.refresh()

# variables

clock = pygame.time.Clock()
playtime = 0.0


while playingGame:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break;
	if ev.type == pygame.MOUSEBUTTONDOWN:
		x, y = ev.pos
		x /= SPOT
		y /= SPOT
		position = 	((x), (y))

		if position == selectedPiece:
			possibleMoves = []
			selectedPiece = (9, 9) 

		elif position in possibleMoves:
			mainBoard.spaces[selectedPiece[1]][selectedPiece[0]].move(position)
			if turn == "black":
				turn = "white"
			elif turn == "white":
				turn = "black"
			possibleMoves = []
			selectedPiece = (9, 9)

		else:
			try:
				possibleMoves = []
				print turn
				if mainBoard.spaces[y][x].color == turn:
					for i in mainBoard.spaces[y][x].moves(position):
						possibleMoves.append(i)
					print "possibleMoves: " + str(possibleMoves)
				selectedPiece = position
				
			except AttributeError:
				pass

		mainBoard.refresh()

finale = end.render("%s WINS!" % winner, True, red)
screen.blit(finale, (90, 350))
pygame.display.flip()

while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break;

