import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("Assignment3")
import parallax
para = parallax.Parallax(screen,"parallax_IMGS/Background_IMGS/", 7, 0, [(0,0), (0,807), (0,624), 
																  (0,805), (0,831), (0,951), (0,1684)])

#init
para.resize_layers()


# Main loop
run = True
while run:
    clock.tick(30)
    print(int(clock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.VIDEORESIZE:
            para.resize_layers()
    para.handle_event(event)

    
    screen.fill((0, 0, 0))
    para.draw()
   

    # Update the display
    pygame.display.flip()

pygame.quit()