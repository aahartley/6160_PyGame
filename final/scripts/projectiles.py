import pygame
import scripts.animations as ani
import math
import scripts.utils as utils
class Projectile:
    def __init__(self, attack_animation, pos, mouse_pos, bow_pos):
        #self.attack_animation = attack_animation
        #self.image, self.shadow_image = self.attack_animation.get_current_frames()
        #self.mask = pygame.mask.from_surface(self.image)
        #self.rect = self.image.get_bounding_rect()
        #self.position = pygame.Vector2(bow_pos)
        self.position = pos
        #self.position[1] -=30

        self.speed = 500
        self.target_position = pygame.Vector2(mouse_pos)
        self.angle = self.calculate_angle(self.position, self.target_position)
        self.real_angle = self.calc_real_angle(pos, self.target_position)
        self.sheet = attack_animation
        self.sheet = pygame.transform.rotate(self.sheet, -self.real_angle).convert_alpha()
        self.mask = pygame.mask.from_surface(self.sheet)
        self.rect = self.sheet.get_bounding_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]
        #print(self.angle)
        self.direction_vector = pygame.Vector2(self.target_position - self.position)
        self.hit = False
        self.fire = False
        self.local_centroid = pygame.Vector2(self.mask.centroid())
        self.local_centroid[0] -= 10
        #self.drawing_rect = self.image.get_rect()
        self.drawing_rect = self.sheet.get_rect()

    
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
                    #self.hit = False
                    #self.target_position = None  # Stop movement when the target is reached

                else:
                    self.position += direction * distance_to_move
            #self.attack_animation.update(dt, self.angle)       

#might need to pos arrow to more center to curosr??
    def draw(self, screen):
        if self.fire:
            #self.image, self.shadow_image = self.attack_animation.get_current_frames()
            #self.mask = pygame.mask.from_surface(self.image)
            self.mask = pygame.mask.from_surface(self.sheet)

            #self.rect = self.image.get_bounding_rect()
            #self.rect.center = self.position
            self.rect = self.sheet.get_bounding_rect()
            self.rect.center = self.position
            self.local_centroid = pygame.Vector2(self.mask.centroid())  # local space
            #self.local_centroid[0] += 10
            #self.drawing_rect = self.image.get_rect()
            self.drawing_rect = self.sheet.get_rect()

            #distance from pos to (0,0) topleft corner
            offset_x = self.position[0] - self.local_centroid[0]
            offset_y = self.position[1] - self.local_centroid[1] 

            self.drawing_rect.x = offset_x
            self.drawing_rect.y = offset_y

            # screen.blit(self.shadow_image, self.drawing_rect)
            # screen.blit(self.image, self.drawing_rect)
            #screen.blit(self.sheet, self.drawing_rect)
            screen.blit(self.sheet, self.drawing_rect)
            #pygame.draw.rect(screen, (0,255,0),self.rect , 1)
            #pygame.draw.rect(screen, (0,255,0),self.drawing_rect , 1)
            #pygame.draw.circle(screen, (0, 255, 0), (self.drawing_rect.x + self.local_centroid[0], self.drawing_rect.y + self.local_centroid[1]), 3)

    def calculate_angle(self, position, target_position):
        direction_vector = target_position - position
        radians = math.atan2(direction_vector.y, direction_vector.x)  
        angle = math.degrees(radians) % 360 
        angle = (angle+90) % 360
        return angle

        
    def calc_real_angle(self, position, target_position):
        direction_vector = target_position - position
        radians = math.atan2(-direction_vector.y, direction_vector.x)
        angle = (90- math.degrees(radians) ) % 360  
        return angle

