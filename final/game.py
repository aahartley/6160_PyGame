import pygame
import sys

from scripts.utils import load_image, load_images
#from scripts.entities import PhysicsEntity
#from scripts.particles 

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Definitely NOT nightcrawler')

        self.width, self.height = 640, 480
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.display = pygame.Surface((int(self.width//2),int(self.height//2)))

        self.clock = pygame.time.Clock()

        self.movement = [False, False]

        self.assets = {
            'player': load_image('entities/player.png')
            #'background': load_image('background.png'),

        }
        #self.player = PhysicsEntity(self, 'player', (50,50), (8,15))


    def run(self):
        running = True
        frames = 0
        while running:
            dt = self.clock.tick(60)/1000

            #fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))

            self.display.fill('black')
            #self.display.blit(self.assets['background'], (0,0))
            #screen.blit(fps_text,(0,0))
        

            # self.player.update(self.movement[1] - self.movement[0],  0)
            # self.player.render(self.display)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        pass
                        #self.player.vel[1] = -3

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    #print(screen.get_at(mouse_pos))

          

            
            frames += 1
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))#scale up for pixel look
            pygame.display.update()
            #tick here?

Game().run()
