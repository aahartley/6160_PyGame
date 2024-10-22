import pygame
import scripts.animations as ani
import math
class Projectile:
    def __init__(self, attack_animation, pos, mouse_pos):
        self.attack_animation = attack_animation
        self.image, self.shadow_image = self.attack_animation.get_current_frames()
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(pos)
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]
        self.speed = 500
        self.target_position = pygame.Vector2(mouse_pos)
        self.angle = self.calculate_angle(self.position, self.target_position)
        print(self.angle)
        self.direction_vector = pygame.Vector2(self.target_position - self.position)
        self.hit = False
        self.fire = False

    
    def update(self, dt):
        #print(direction_vector)
        if self.fire:
            if self.direction_vector.length() > 0:  # Check if the vector is non-zero
                direction = self.direction_vector.normalize()  # Get the direction
                distance_to_move = self.speed * dt  # Distance to move in this frame
                distance_to_target = self.position.distance_to(self.target_position)

                # If close enough, stop moving
                if distance_to_move >= distance_to_target:
                    self.position = self.target_position
                    self.hit = True
                    #self.target_position = None  # Stop movement when the target is reached

                else:
                    self.position += direction * distance_to_move
            self.attack_animation.update(dt, self.angle)       


    def draw(self, screen):
        if self.fire:
            self.image, self.shadow_image = self.attack_animation.get_current_frames()
            self.rect = self.image.get_rect()
            self.rect.centerx = self.position[0]+50
            self.rect.centery = self.position[1]-30
            topleft = self.rect.topleft
            #screen.blit(self.shadow_image, (topleft[0]-1, topleft[1]-1))
            screen.blit(self.shadow_image, self.rect)
            #screen.blit(self.image, (topleft[0]-1, topleft[1]+25))
            screen.blit(self.image, self.rect)
            #pygame.draw.rect(screen, (0,255,0),self.rect , 1)

    def calculate_angle(self, position, target_position):
        direction_vector = target_position - position
        radians = math.atan2(direction_vector.y, direction_vector.x)  
        angle = math.degrees(radians) % 360 
        angle = (angle+90) % 360
        return angle