import pygame
from sys import exit
pygame.init()

screenSize = (800,600)

display = pygame.display.set_mode(screenSize)


FPS = 60
clock = pygame.time.Clock()
isgame = True

class Ball:
	def __init__(self, pos):
		self.pos = pos
		self.xPos = self.pos[0]
		self.yPos = self.pos[1]
		self.velociety = 3

	def move(self):
		if self.xPos > screenSize[0]:
			self.velociety = -self.velociety
		if self.xPos < 0:
			self.velociety = -self.velociety
		self.xPos+=1*self.velociety

	def draw(self):
		self.move()
		
		pygame.draw.circle(display, (255,255,255), (self.xPos, self.yPos), 10)

balls = []
while isgame:
	display.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			isgame = False
			break
		if event.type == pygame.KEYDOWN:
			if event.key == 27:
				isgame = False
				break
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				ball = Ball(pygame.mouse.get_pos())
				balls.append(ball)


	clock.tick(FPS)
	for unit in balls:
		unit.draw()
	pygame.display.flip()