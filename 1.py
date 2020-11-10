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
		


while isgame:
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
				a = Ball(i)
				print(pygame.mouse.get_pos())


	clock.tick(FPS)
	pygame.display.update()