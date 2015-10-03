import pygame, sys
from pygame.locals import *

pygame.init()
class GameObject:
	def __init__(self, image, height, speed):
		self.speed = speed+1
		self.gravity = speed+3
		self.image = image
		self.pos = image.get_rect().move(0, height)
	def move(self):
		self.pos = self.pos.move(self.speed, self.gravity)
		if self.pos.right > 1024 or self.pos.left < 0:
			self.speed = -self.speed
		if self.pos.bottom > 768 or self.pos.top < 0:
			self.gravity = -self.gravity

screen = pygame.display.set_mode((1024, 768))
player = pygame.image.load('baseball.png').convert_alpha()
background = pygame.image.load('sky.jpg').convert()
screen.blit(background, (0,0))
objects = []
for x in range(10):
	o = GameObject(player, x*60, x)
	objects.append(o)
while 1:
	for event in pygame.event.get():
		if event.type in (QUIT, KEYDOWN):
			sys.exit()
	for o in objects:
		screen.blit(background, o.pos, o.pos)
	for o in objects:
		o.move()
		screen.blit(o.image, o.pos)
	pygame.display.update()
	pygame.time.delay(100)
