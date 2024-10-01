import pygame
import random
from scripts.utils import load_image, load_images, scale_image



class Particle:
    def __init__(self, pos, vel, color, radius, img):
        self.pos = pos
        self.vel = vel
        self.color = color
        self.alpha = 255
        self.alpha_rate = 3
        self.radius = radius
        self.alive = True
        self.time = 0
        self.size = 0.1
        self.og_img = img
        self.img = scale_image(img, self.size)
        self.damping = 0.99
    
    def update(self, dt):
        if self.alive:
            self.size += 0.05 * dt
            self.alpha -= self.alpha_rate
            if(self.alpha < 0):
                self.alpha = 0
                self.alive = False

            self.alpha_rate -= 50 * dt
            if self.alpha_rate < 50 * dt:
                self.alpha_rate = 50 *dt
            self.img = scale_image(self.og_img, self.size)
            self.img.set_alpha(self.alpha)

            self.vel[0] += random.choice((-10+self.time*-30,10+self.time*30)) * dt
            self.vel[1] += random.choice((-8, -5)) * dt * self.damping
            self.pos[0] += (self.vel[0] * dt)
            self.pos[1] += (self.vel[1] * dt)

            self.time += dt
            if self.time >= 20 :
                self.alive = False
        
    def draw(self, screen):
        if self.alive:
            #pygame.draw.circle(screen, self.color, self.pos, self.radius)
            screen.blit(self.img, self.img.get_rect(center = self.pos))


class ParticleEmitter:
    def __init__(self, pos, rate, max, img):
        self.particles = []
        self.pos = pos
        self.rate = rate
        self.max = max
        self.img = img
        self.alive = True
        self.time = 0

    def update(self, dt):
        self.time += dt
        rate_per_frame = int(self.rate * self.time)
        if(rate_per_frame > 0):
            rate_check = (self.max - len(self.particles)) - rate_per_frame
            if rate_check >= 0:
                self.emit(rate = rate_per_frame)
            else:
                self.emit(rate = self.max - len(self.particles))
            self.time -= rate_per_frame / self.rate
        

    def emit(self, rate):
        for i in range(rate):
            v_x = random.randint(-1, 1)
            v_y = random.randint(-5, -1)

            r_x = random.randint(1,4)
            r_y = random.randint(1,4)
            self.particles.append(Particle([self.pos[0] + r_x, self.pos[1] - r_y], [0 ,-40 + v_y] , [0,0,255], 2, self.img))
