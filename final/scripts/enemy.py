import pygame
import scripts.utils as utils
import math
import scripts.animations as ani
class Enemy(pygame.sprite.Sprite):
 
    def __init__(self, position, scale):
        super().__init__()

        self.animations = {
            'idle': ani.Animation(utils.enemy_paths[0], utils.enemy_shadow_paths[0], utils.sprite_frame_dict(5, 4, 256, 256), 30, False,0),
            'walk': ani.Animation(utils.enemy_paths[1], utils.enemy_shadow_paths[1], utils.sprite_frame_dict(5, 4, 256, 256), 60, False, 0),
            'attack': ani.Animation(utils.enemy_paths[2],utils.enemy_shadow_paths[2], utils.sprite_frame_dict(5, 4, 256, 256), 100, False, 0)
        }
        self.current_animation = self.animations['idle']
        self.image, self.shadow_image = self.current_animation.get_current_frames()
        self.position = pygame.Vector2(position) 
        self.speed = 100
        self.target_position = None
        self.state = 'idle'     
        self.angle = 0
        self.real_angle = 90
        self.drawing_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_bounding_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]       
        self.local_centroid = pygame.Vector2(self.mask.centroid())


    def change_state(self, state, reset):
        if reset:
            self.animations[self.state].reset()
        self.state = state
        self.current_animation = self.animations[self.state]

    def update(self, dt, target_position):
        self.target_position = target_position
        if self.state == 'attack':
            if self.current_animation.check_loop():
                self.change_state('idle', True)

        elif self.target_position:
                direction_vector = pygame.Vector2(self.target_position - self.position)
                #print(direction_vector)
                if direction_vector.length() > 0:  # Check if the vector is non-zero
                    self.angle = self.calculate_angle(self.position, self.target_position)
                    direction = direction_vector.normalize()  # Get the direction
                    distance_to_move = self.speed * dt  # Distance to move in this frame
                    distance_to_target = self.position.distance_to(self.target_position)

                    # If close enough, stop moving
                    if distance_to_move >= distance_to_target:
                        self.position = self.target_position 
                        self.target_position = None  # Stop movement when the target is reached
                        self.change_state('idle', True)

                    else:
                        self.position += direction * distance_to_move 
                        self.change_state('walk', False)
                        
        self.current_animation.update( dt, self.angle)       

     

    def draw(self, screen):

        self.image, self.shadow_image = self.current_animation.get_current_frames()

        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_bounding_rect()
        self.rect.center = self.position
        self.local_centroid = pygame.Vector2(self.mask.centroid())  # local space
        self.local_centroid[1] += 10
        self.drawing_rect = self.image.get_rect()
        #distance from pos to (0,0) topleft corner
        offset_x = self.position[0] - self.local_centroid[0]
        offset_y = self.position[1] - self.local_centroid[1]

        self.drawing_rect.x = offset_x
        self.drawing_rect.y = offset_y

        screen.blit(self.shadow_image, self.drawing_rect)
        screen.blit(self.image, self.drawing_rect)


        # bow_pos = pygame.Vector2(local_centroid)
        # bow_pos[0] += 50
        # bow_pos[1] -= 25
        # calc_real_angle = self.calc_real_angle(bow_pos,local_centroid )
        # available_angles = list(self.current_animation.sheets.keys())
        # closest_angle = min(available_angles, key=lambda x: abs(x - (calc_real_angle))) 
        # print(closest_angle)
        # bow_pos[0] = math.cos(math.radians(closest_angle)) * (bow_pos[0]-local_centroid[0]) - math.sin(math.radians(closest_angle)) * (bow_pos[1]-local_centroid[1]) + local_centroid[0]
        # bow_pos[1] = math.sin(math.radians(closest_angle)) * (bow_pos[0]-local_centroid[0]) + math.cos(math.radians(closest_angle)) * (bow_pos[1]-local_centroid[1]) + local_centroid[1]

        #pygame.draw.circle(screen, (0, 255, 0), (self.drawing_rect.x + self.bow_pos[0], self.drawing_rect.y + self.bow_pos[1]), 2)



        #pygame.draw.line(screen, (0, 255, 0), p.position, p.target_position)

        # pygame.draw.circle(screen, (255, 0, 0), self.position, 3) 
        #pygame.draw.circle(screen, (0, 255, 0), (self.drawing_rect.x + self.local_centroid[0], self.drawing_rect.y + self.local_centroid[1]-30), 3)

        #pygame.draw.circle(screen, (0, 255, 0), (drawing_rect.x + bow_pos[0], drawing_rect.y + bow_pos[1]), 2)

    




    def handle_event(self, event):
        pass

 
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

