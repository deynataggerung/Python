class Deck(object):
	def __init__(self):
		self.size = 52
		self.cards = []
	def create(self):
		for f in range(1,5):
			for i in range(1,14):
				self.cards.append(Card(i, f))

class Card(object):
	def __init__(self, num, s):
		self.value = num
		suit_defs= {1: "clubs", 2: "diamonds", 3: "hearts", 4: "spades"}
		self.suit = suit_defs[s]



deck = Deck()
Deck.create()
print Deck
print Deck[1]
