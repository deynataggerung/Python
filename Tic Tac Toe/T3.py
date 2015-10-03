import pygame
from math import pi
from random import randint


#I have a bug where certain magic_tup aren't getting removed, or at least that's my guess because it thinks that O can win even though x has already taken the win spot. Check in the don't lose and try to win sections for what's up. Also might be a deletion error 
#x|x|
# |O|
# |O|x

def test(record):
	if len(record) >= 3:
		for a in record:
			for b in record:
				for c in record:
					if a!=b and (a!=c and b!=c):
						if a+b+c == 15:
							return True

#Important for starting
pygame.init()

#Define colors using RGB
white = (255,255,255)
black = (0,0,0)

#create screen
screen = pygame.display.set_mode([600, 620])
pygame.display.set_caption("Tic Tac Toe")

#Start main loop
playing = True
clock = pygame.time.Clock()

#Add Font
comment = pygame.font.SysFont("Times", 20)
end = pygame.font.SysFont("Times", 150)

# Create a place to store previous moves for checking win.
xmoves = []
omoves = []
pos_moves = []
for a in range(0,3):
	for b in range(0,3):
		pos_moves.append([a, b])
pos_magic = []
for a in range(0,3):
	for b in range(0,3):
		pos_magic.append((a,b))
xwin = []
owin = []
winner = False
moves = 0

#Defines the magic square
magic = {(0,0):4,(0,1):3,(0,2):8,(1,0):9,(1,1):5,(1,2):1,(2,0):2,(2,1):7,(2,2):6}

#Set up comparison for tuples vs lists
conv = {(0,0):[0,0],(0,1):[0,1],(0,2):[0,2],(1,0):[1,0],(1,1):[1,1],(1,2):[1,2],(2,0):[2,0],(2,1):[2,1],(2,2):[2,2]}

player = "x"

while playing:
	clock.tick(10)


	region = [9,9]
	magic_tup = False
	magic_num = 0
	valid = False
	#Set it up so the loop ends on quitting
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break

	#Player Move
	if player == "x":

		#Look for click
		if ev.type == pygame.MOUSEBUTTONDOWN:
			position = ev.dict["pos"]
			fix = {0:200,200:400,400:600} #Allows for a proper range
			#finds region of mouse click
			for x in [0, 200, 400]:
				for y in [0, 200, 400]:
					if position[0] in range(x, fix[x]) and position[1] in range(y, fix[y]):
						region = [x/200, y/200]
						magic_tup = (x/200, y/200)
						magic_num = magic[magic_tup]
						valid = True


	#Computer Move
	elif player == "o":		
		part1 = randint(0,2)
		part2 = randint(0,2)
		region = [part1, part2]
		magic_tup = (part1, part2)
		magic_num = magic[magic_tup]
		valid = True
		print region
		print pos_magic
		#Don't lose
		for i in pos_magic:
			test_xwin = list(xwin)
			test_xwin.append(magic[i])
			if test(test_xwin):
				region = conv[i]
				magic_tup = i
				magic_num = magic[i]
				valid = True
				unsure = False

		#Try to win
		for i in pos_magic:
			test_owin = list(owin)
			test_owin.append(magic[i])
			if test(test_owin):
				print "o could win"
				region = conv[i]
				magic_tup = i
				magic_num = magic[i]
				valid = True
				unsure = False
		print region

	#Check to see if move is valid and then make it
	if valid:
		print "was valid"
		if region not in xmoves and region not in omoves:
			print "xmove", xmoves
			print "omove", omoves
			if player == "x":
				print "x"
				#Upadate game info x
				xmoves.append(region)
				pos_moves.remove(region)
				xwin.append(magic_num)
				pos_magic.remove(magic_tup)
				player = "o"
			elif player == "o":
				print "o"
				#Upadate game info o
				omoves.append(region)
				pos_moves.remove(region)
				owin.append(magic_num)
				pos_magic.remove(magic_tup)
				player = "x"
			moves += 1


	#Check for ending condition
	if test(xwin):
		playing= False
		winner = "X"

	if test(owin):
		playing= False
		winner = "O"

	if moves >= 9:
		playing = False
	
	#Draw the Board
	pygame.draw.line(screen, black, [0,200], [600,200], 10)
	pygame.draw.line(screen, black, [0,400], [600,400], 10)
	pygame.draw.line(screen, black, [200,0], [200,600], 10)
	pygame.draw.line(screen, black, [400,0], [400,600], 10)
	screen.fill(white)
	
	#Draw all moves
	for x in xmoves:
		pygame.draw.line(screen, black, [(x[0]*200)+20, (x[1]*200) +20], [(x[0]*200)+180, (x[1]*200)+180], 8)
		pygame.draw.line(screen, black, [(x[0]*200)+20, (x[1]*200) +180], [(x[0]*200)+180, (x[1]*200)+20], 8)
	for o in omoves:
		pygame.draw.circle(screen, black, [(o[0]*200)+100, (o[1]*200) +100], 80, 8)
	pygame.draw.line(screen, black, [0,200], [600,200], 10)
	pygame.draw.line(screen, black, [0,400], [600,400], 10)
	pygame.draw.line(screen, black, [200,0], [200,600], 10)
	pygame.draw.line(screen, black, [400,0], [400,600], 10)
	
	finale = comment.render("You're playing Tic Tac Toe", True, black)
	screen.blit(finale, [0,600])
	pygame.display.flip()

screen.fill(white)

if winner:
	ending = end.render(winner + " WINS!", True, black)
	screen.blit(ending, [20, 225])
else:
	ending = end.render("TIE", True, black)
	screen.blit(ending, [200, 225])
pygame.display.flip()

while True:
	ev = pygame.event.poll()
	if ev.type == pygame.QUIT:
		pygame.quit()
		break
	if ev.type == pygame.KEYDOWN:
		for x in xmoves:
			pygame.draw.line(screen, black, [(x[0]*200)+20, (x[1]*200) +20], [(x[0]*200)+180, (x[1]*200)+180], 8)
			pygame.draw.line(screen, black, [(x[0]*200)+20, (x[1]*200) +180], [(x[0]*200)+180, (x[1]*200)+20], 8)
		for o in omoves:
			pygame.draw.circle(screen, black, [(o[0]*200)+100, (o[1]*200) +100], 80, 8)
		pygame.draw.line(screen, black, [0,200], [600,200], 10)
		pygame.draw.line(screen, black, [0,400], [600,400], 10)
		pygame.draw.line(screen, black, [200,0], [200,600], 10)
		pygame.draw.line(screen, black, [400,0], [400,600], 10)
	
		finale = comment.render("You're playing Tic Tac Toe", True, black)
		screen.blit(finale, [0,600])
		pygame.display.flip()
	
	
