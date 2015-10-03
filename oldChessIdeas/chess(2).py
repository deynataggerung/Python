
#Remember that all x inputs must be the actual spot of that piece, not the piece number.
class Pawn(object):
	def __init__(self, x, color):
		if color == "black":
			y = 1
		elif color == "white":
			y = 8
		else:
			return False
		self.position = [x, y]
	
	def position(self):
		return self.position

class Rook(object):
	def __init__(self, x, color):
		if color == "black":
			y = 1
		elif color == "white":
			y = 8
		else:
			return False
		self.position = (x,y)
	
	def position(self):
		return self.position

class Knight(object):
	def __init__(self, x, color):
		if color == "black":
			y = 1
		elif color == "white":
			y = 8
		else:
			return False
		self.position = (x, y)
	
	def position(self):
		return self.position

class Bishop(object):
	def __init__(self, x, color):
		if color == "black":
			y = 1
		elif color == "white":
			y = 8
		else:
			return False
		self.position = (x, y)
	
	def position(self):
		return self.position

class King(object):
	def __init__(self, color):
		if color == "black":
			y = 1
		elif color == "white":
			y = 8
		else:
			return False
		self.position = (4, y)

	def position(self):
		return self.position

class Queen(object):
	def __init__(self, color):
		if color == "black":
			y = 1
		elif color =="white":
			y = 8
		else:
			return False
		self.position = (4,y)

	def position(self):
		return self.position


black = {}
for f in range(1,9):
	black[f] = Pawn(f, "black")

print black

print black[5].position()

class Board(object):
	def __init__(self, piece):
		self.pieces = piece
		self.translator = {1:2, 2:4, 3:6, 4:8, 5:10, 6:12, 7:14, 8:16}
		self.display = [[' ', '| 1 ', '| 2 ', '| 3 ', '| 4 ', '| 5 ', '| 6 ', '| 7 ', '| 8 ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['1', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['2', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['3', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['4', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['5', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['6', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['7', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|'],['8', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|   ', '|'],[' ','|___','|___','|___','|___','|___','|___','|___','|___','|']]

	def setup(self):
		for i in self.pieces:
			i[0] = self.translator[i[0]]

	def show(self):
		for i in self.display:
			print " ".join(i)







