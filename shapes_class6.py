import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pygame Drawing Shapes')

# Colors (R, G, B) and with Alpha
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (128, 0, 128)

# Colors with alpha for transparency
transparent_red = (255, 255, 255, 128)  # 50% transparent red
transparent_green = (0, 255, 0, 128)  # 50% transparent green

# Surface for alpha shapes
alpha_surface = pygame.Surface((width, height), pygame.SRCALPHA)

# Function to save the current screen as a PNG image
def save_screenshot(filename='screenshot.png'):
    pygame.image.save(screen, filename)
    print(f"Screenshot saved as {filename}")

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                save_screenshot()  # Save screenshot when 'S' key is pressed

    # Fill background with black
    screen.fill((0, 0, 0))

    # Draw a polygon
    pygame.draw.polygon(screen, red, [(100.01, 100), (150, 50), (200, 100), (175, 150), (125, 150)])

    # Draw a line
    pygame.draw.line(screen, green, (50, 300), (200, 300), 5)

    # Draw a circle
    pygame.draw.circle(screen, blue, (400, 150), 50)

    # Draw a rectangle
    pygame.draw.rect(screen, yellow, (500, 100, 150, 75))

    # Draw an ellipse
    pygame.draw.ellipse(screen, purple, (600, 300, 150, 75))

    # Draw a transparent red rectangle
    pygame.draw.rect(alpha_surface, transparent_red, (50, 400, 100, 50))

    # Draw a transparent green ellipse
    pygame.draw.ellipse(alpha_surface, transparent_green, (200, 400, 100, 50))

    # Blit the transparent shapes to the main screen
    screen.blit(alpha_surface, (0, 0))

    # Update display
    pygame.display.flip()
