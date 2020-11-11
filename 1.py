import pygame
from sys import exit
pygame.init()

screenSize = (800,600)

display = pygame.display.set_mode(screenSize)
H_WIDTH = screenSize[0]/2
H_HEIGHT = screenSize[1]/2
FPS = 120
clock = pygame.time.Clock()
isgame = True

class Ball:
	def __init__(self, pos):
		self.pos = pos
		self.xPos = self.pos[0]
		self.yPos = self.pos[1]
		if self.xPos < H_WIDTH:
			self.velocietyX = -1
		if self.xPos > H_WIDTH:
			self.velocietyX = 1
		if self.yPos < H_HEIGHT:
			self.velocietyY = -1
		if self.yPos>H_HEIGHT:
			self.velocietyY = 1
	def move(self):
		if self.xPos+10 > screenSize[0]:
			self.velocietyX = -self.velocietyX
		if self.xPos-10 < 0:
			self.velocietyX = -self.velocietyX

		if self.yPos+10 > screenSize[1]:
			# self.velocietyY = 4
			self.velocietyY = -self.velocietyY
		if self.yPos-10 < 0 :
			self.velocietyY = -self.velocietyY

		self.xPos+=1*self.velocietyX
		self.yPos+=1*self.velocietyY
		# self.velocietyY+=0.1
		print(self.velocietyY)

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