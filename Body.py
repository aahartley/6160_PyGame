import pygame
import random
import math
from Particle import Particle, ParticleEmitter

class Body:
    def __init__(self, vel,com, particles):
        self.vel = vel
        self.com = com
        self.particles = particles
        for p in self.particles:
            p.distance[0] = p.pos[0] - self.com[0]
            p.distance[1] = p.pos[1] - self.com[1]
        self.separated = False

    def draw(self, screen):
        for p in self.particles:
            # if(not p.rigid):
            #     print("not rigid")
            pygame.draw.circle(screen, p.color,p.pos,p.radius)
        
    def update(self, frames, dt):
        if(frames < 200):
            self.vel[0] += 0 *dt
            # p.vel[1] += random.uniform(-10, 10) *dt
            #p.vel[1] += random.choice([-10, 10]) * dt
            # self.vel[1] += 10 * dt

        # else:
        #     vel[1] = (orig_pos[sum][1] - p.pos[1]) * 1000 * dt

        self.com[0] += round(self.vel[0] *dt)
        self.com[1] += round(self.vel[1] *dt)
        if(self.com[0] <= 0):
            self.com[0] = 0
        if(self.com[0] >= 800):
            self.com[0] = 800
        if(self.com[1] <= 0):
            self.com[1] = 0
        if(self.com[1] >= 600):
            self.com[1] = 600
        if(not self.separated):
            for p in self.particles:
                if(p.rigid== False):
                    target_x =  p.distance[0] + self.com[0] 
                    target_y = p.distance[1] + self.com[1] 
                    p.pos[0] += (target_x - p.pos[0]) * 5 * dt
                    p.pos[1] += (target_y - p.pos[1])* 5 * dt
                    if(int(round(p.pos[0]))==int(target_x) and int(round(p.pos[1]))==int(target_y)):
                        p.rigid = True
                elif(p.rigid):
                    p.pos[0] = p.distance[0] + self.com[0] 
                    p.pos[1] = p.distance[1] + self.com[1] 
        if(self.separated):
            for p in self.particles:
                p.vel[0] += random.uniform(-1000,1000) * dt
                p.vel[1] += random.uniform(-1000,1000) * dt
                p.pos[0] += p.vel[0] *dt 
                p.pos[1] += p.vel[1] * dt

    def separate(self):
        self.separated = not self.separated
        for p in self.particles:
            # target_x =  p.distance[0] + self.com[0] 
            # target_y = p.distance[1] + self.com[1]
            # if(p.pos[0]!=target_x and p.pos[1]!=target_y):
            p.rigid = False
    
