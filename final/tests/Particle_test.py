import pygame
import sys
import os
import random
from Particle import Particle, ParticleEmitter

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Drawing Shapes')

# Colors (R, G, B) and with Alpha
red = (255, 0, 0)
green = (0, 255, 0)
grass = (124, 252, 0)
blue = (0, 0, 255)
yellow = (212,175,55)
purple = (128, 0, 128)
dark_beige = (217,174,128)
black = (0,0,0)
white = (255,255,255)
night_sky = (19,24,98)
darker_sky = (17,19,56)
brown = (139,69,19)
door = (128,117,115)
blue_water = (153,192,227)
dim_gray = (105,105,105)
yellow = (255,255,224)
glass = (216,228,233)
# Colors with alpha for transparency
transparent_red = (255, 255, 255, 128)  # 50% transparent red
transparent_black = (15, 15, 15, 128)  # 50% transparent red
transparent_green = (0, 255, 0, 128)  # 50% transparent green

# Surface for alpha shapes
alpha_surface = pygame.Surface((width, 400), pygame.SRCALPHA)


# Function to save the current screen as a PNG image
def save_screenshot(filename='screenshot.png'):
    pygame.image.save(screen, filename)
    print(f"Screenshot saved as {filename}")

clock = pygame.time.Clock()

particles = []
emitters = [ParticleEmitter([0,0])]

# Main loop
running = True
frames = 0
while running:
    dt = clock.tick(60)/1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_screenshot()  # Save screenshot when 'S' key is pressed
            # elif event.key == pygame.K_SPACE:
            # elif event.key == pygame.K_LEFT:
            # elif event.key == pygame.K_RIGHT:
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            print(mouse_pos)
            #print(screen.get_at(mouse_pos))

    fps_text = font.render(f"FPS: {int(clock.get_fps())}", True, (255, 255, 255))
    # Fill background with black
    screen.fill(black)
    screen.blit(fps_text,(0,0))

    
    frames += 1
    # Update display
    pygame.display.flip()

pygame.quit()
sys.exit()
