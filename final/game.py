import pygame
import sys
import time
from scripts.utils import load_image, load_images
from scripts.particles import Particle, ParticleEmitter
import scripts.sims as sims
import scripts.particle_emitters as pe
import scripts.player as char
import scripts.tiles as tile
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('part icles')

        self.width, self.height = 1280, 720
        self.screen = pygame.display.set_mode((self.width, self.height))


        self.clock = pygame.time.Clock()

        self.assets = {
            "smoke" : load_image("particles/smoke.png")
        }
        self.font = pygame.font.Font(None, 36)
        self.particle_emitters = [ParticleEmitter([self.width//2, self.height-100], 100, 1000, self.assets["smoke"])]

        # self.smoke_sim = sims.create_smoke_sim()
        # self.smoke_sim.add_emitter(pe.ParticleEmitter([self.width//2,self.height-100], 'random'))

        self.player = char.Character([self.width//2, self.height//2])
        self.floor = tile.Tile(self.width, self.height)


    def run(self):
        running = True
        frames = 0
        particles = 0
        while running:
            dt = self.clock.tick(60)/1000

            fps_text = self.font.render(f"FPS: {int(self.clock.get_fps())}", True, (255, 255, 255))

            self.screen.fill((0,0,0))
            self.floor.draw(self.screen)

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
                    # mouse_pos = pygame.mouse.get_pos()
                    # print(mouse_pos)
                    pass
                self.player.handle_event(event)
                          
            self.player.update(dt)
            self.player.draw(self.screen)
            # pygame.draw.rect(self.screen, (255,0,0), self.player.rect, 1)
            # pygame.draw.line(self.screen, (255,0,0), (self.width//2, 0), (self.width//2,self.height))
            # pygame.draw.line(self.screen, (255,0,0), (0, self.height//2), (self.width,self.height//2))
            # start_time = time.time()  # Start timer
            # self.smoke_sim.update(dt)
            # self.smoke_sim.draw(self.screen)
            # end_time = time.time()  # End timer
            # smoke_sim_time += end_time-start_time

            # start_time = time.time()  # Start timer
            for pe in self.particle_emitters:
                pe.update(dt)
                for p in pe.particles:
                    p.update(dt)
                    p.draw(self.screen)
                    particles += 1
            # end_time = time.time()  # End timer
            # smoke_sim_time += end_time-start_time

       
            #particle_text = self.font.render(f"Particles: {self.smoke_sim.get_nb()}", True, (255, 255, 255))
            #particle_text2 = self.font.render(f"Particles: {particles}", True, (255, 255, 255))

            #self.screen.blit(particle_text,(0,30))
            #self.screen.blit(particle_text2,(0,30))
            particles = 0
    

            frames += 1
    
            pygame.display.update()

Game().run()
