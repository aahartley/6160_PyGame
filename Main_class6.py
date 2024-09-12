import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400,400))

caption = pygame.display.set_caption("CPSC 4161 6160")

WHITE 	= 255,255,255
RED 	= 255,0,0
GREEN 	= 0,255,0 


running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	screen.fill((WHITE))

	#polygon(surface, color, points)
	pygame.draw.polygon(screen, (255,0,0), [(80, 80), (180, 80), (180, 150),(80,150)])
			
	#circle(surface, color, center, radius)			
	pygame.draw.circle(screen, (0,0,255), (200,200), 100)	
	
	#ellipse(surface, color, rect)
	pygame.draw.ellipse(screen, RED, (200, 25,24,100))		
			
	#line(surface, color, start_pos, end_pos)
	pygame.draw.line(screen, GREEN, (0,0),(400,400),100)


	pygame.display.update()
	
pygame.quit()
sys.exit()
