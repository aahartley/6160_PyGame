import pygame
import sys

from scripts.utils import load_image, load_images
from scripts.particles import Particle, ParticleEmitter

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('part icles')

        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))


        self.clock = pygame.time.Clock()

        self.assets = {
            "smoke" : load_image("particles/smoke.png")
        }
        self.font = pygame.font.Font(None, 36)
        self.particle_emitters = [ParticleEmitter([self.width//2, self.height-100], 100, 1000, self.assets["smoke"])]

      


    def run(self):
        running = True
        frames = 0
        particles = 0
        while running:
            dt = self.clock.tick(60)/1000

            fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))

            self.screen.fill((0,0,0))
            self.screen.blit(fps_text,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pass
                    if event.key == pygame.K_RIGHT:
                        pass
                    if event.key == pygame.K_UP:
                        pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    print(mouse_pos)
                    #print(screen.get_at(mouse_pos))           

            for pe in self.particle_emitters:
                pe.update(dt)
                for p in pe.particles:
                    p.update(dt)
                    p.draw(self.screen)
                    particles += 1

            paritlce_text = self.font.render(f"Particles: {particles}", True, (255, 255, 255))
            self.screen.blit(paritlce_text,(0,30))
            particles = 0
    

            frames += 1
            pygame.display.update()

   
Game().run()