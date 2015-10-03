import pygame
from math import pi
from random import randint

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
xwin = []
owin = []
winner = False
moves = 0

#Defines the magic square
magic = {(0,0):4,(0,1):3,(0,2):8,(1,0):9,(1,1):5,(1,2):1,(2,0):2,(2,1):7,(2,2):6}


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
		playing = False

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

	#Check to see if move is valid and then make it
	if valid:
		if region not in xmoves and region not in omoves:
			if player == "x":
				xmoves.append(region)
				xwin.append(magic_num)
				player = "o"
			elif player == "o":
				omoves.append(region)
				owin.append(magic_num)
				player = "x"
			moves += 1

	if len(xwin) >= 3:
		for a in xwin:
			for b in xwin:
				for c in xwin:
					if a!=b and (a!=c and b!=c):
						if a+b+c == 15:
							print "a", a
							print "b", b
							print "c", c
							print
							playing= False
							winner = "X"

	if len(owin) >= 3:
		for a in owin:
			for b in owin:
				for c in owin:
					if a!=b and (a!=c and b!=c):
						if a+b+c == 15:
							print "a", a
							print "b", b
							print "c", c
							print
							playing= False
							winner = "O"
	if moves >= 9:
		playing = False
	
	screen.fill(white)
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
	if ev.type == pygame.QUIT or ev.type == pygame.KEYDOWN:
		pygame.quit()
		break
	
	
