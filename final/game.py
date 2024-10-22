import pygame
import sys
import time
from scripts.utils import load_image, load_images
from scripts.particles import Particle, ParticleEmitter, BasicParticle
import scripts.sims as sims
import scripts.particle_emitters as pe
import scripts.player as char
import scripts.tiles as tile
import scripts.enemy as en
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
        #self.enemy = en.Enemy([self.width//4,self.height//2])
        #self.pa = BasicParticle([0, self.height//2], [0,0], (255,0,0), 4,3)
        self.pa = BasicParticle([0, self.height//2], [0,0], (255,0,0), 4)


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
                #self.enemy.handle_event(event)
                          
            self.player.update(dt)
            self.player.draw(self.screen)
            pygame.draw.rect(self.screen, (255,0,0), self.player.rect, 1)
            #print(self.player.rect)
            pos = pygame.Rect((self.player.position[0], self.player.position[1],320,320))
            pos.center = self.player.position
            pygame.draw.rect(self.screen, (0,255,0),pos , 1)
            # if self.player.target_position != None:
            #     pygame.draw.line(self.screen, (0,255,0), self.player.position, self.player.target_position)

            # pygame.draw.line(self.screen, (255,0,0), (self.width//2, 0), (self.width//2,self.height))
            # pygame.draw.line(self.screen, (255,0,0), (0, self.height//2), (self.width,self.height//2))
            #self.enemy.update(dt)
            #self.enemy.draw(self.screen)
            
            # start_time = time.time()  # Start timer
            # self.smoke_sim.update(dt)
            # self.smoke_sim.draw(self.screen)
            # end_time = time.time()  # End timer
            # smoke_sim_time += end_time-start_time

            # start_time = time.time()  # Start timer
            # for pe in self.particle_emitters:
            #     pe.update(dt)
            #     for p in pe.particles:
            #         p.update(dt)
            #         p.draw(self.screen)
            #         particles += 1
            # end_time = time.time()  # End timer
            # smoke_sim_time += end_time-start_time
            self.pa.update(dt)
            self.pa.draw(self.screen)
       
            #particle_text = self.font.render(f"Particles: {self.smoke_sim.get_nb()}", True, (255, 255, 255))
            #particle_text2 = self.font.render(f"Particles: {particles}", True, (255, 255, 255))

            #self.screen.blit(particle_text,(0,30))
            #self.screen.blit(particle_text2,(0,30))
            particles = 0
    

            frames += 1
    
            pygame.display.update()

Game().run()
