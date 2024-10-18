import pygame
import scripts.utils as utils
import math
import scripts.animations as ani
class Character(pygame.sprite.Sprite):
    
 
    def __init__(self, position):
        super().__init__()

        self.animations = {
            'idle': ani.Animation(utils.player_paths[0], utils.player_shadow_paths[0], utils.sprite_frame_dict(4, 4, 320, 320), 30),
            'walk': ani.Animation(utils.player_paths[1], utils.player_shadow_paths[1], utils.sprite_frame_dict(4, 6, 320, 320), 60),
            'attack': ani.Animation(utils.player_paths[2],utils.player_shadow_paths[2], utils.sprite_frame_dict(4, 6, 320, 320), 100)
        }
        self.attack_animations = {
            'basic_attack': ani.Animation(utils.prop_paths[0], utils.prop_paths[0],utils.sprite_frame_dict(1,1,1024,1024), 60)
        }
        self.current_animation = self.animations['idle']
        self.current_attack = None
        self.image, self.shadow_image = self.current_animation.get_current_frames()
        self.rect = self.image.get_rect()
        self.position = pygame.Vector2(position)
        self.rect.centerx = position[0]
        self.rect.centery = position[1]
        self.speed = 200
        self.target_position = None
        self.right_click_held = False
        self.state = 'idle'     
        self.angle = 0   
        #rset after each sate?
   
    
    def update(self, dt):

        if self.state == 'attack':
            if self.current_animation.check_loop():
                self.animations[self.state].reset()
                self.state = 'idle'
                self.current_animation = self.animations[self.state]

        elif self.target_position:
                direction_vector = self.target_position - self.position
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
                        self.state = 'idle'
                        self.current_animation = self.animations[self.state]

                    else:
                        self.position += direction * distance_to_move
                        self.state = 'walk'
                        self.current_animation = self.animations[self.state]
                        

        self.current_animation.update(self.state, dt, self.angle)                


  
    
    def draw(self, screen):
        self.image, self.shadow_image = self.current_animation.get_current_frames()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]-100
        topleft = self.rect.topleft
        #screen.blit(self.shadow_image, (topleft[0]-1, topleft[1]-1))
        screen.blit(self.shadow_image, self.rect)
        #screen.blit(self.image, (topleft[0]-1, topleft[1]+25))
        screen.blit(self.image, self.rect)
        if(self.current_attack != None):
            aa_image, aa_shadow_image = self.current_attack.get_current_frames()
            aa_rect = aa_image.get_rect()
            screen.blit(aa_image, aa_rect)



    def handle_event(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    mouse_pos = pygame.mouse.get_pos()
                    self.target_position = pygame.Vector2(mouse_pos)
                    self.right_click_held = True  

            elif event.type == pygame.MOUSEMOTION and self.right_click_held:
                mouse_pos = pygame.mouse.get_pos()
                self.target_position = pygame.Vector2(mouse_pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    self.right_click_held = False
            

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                        self.state = 'idle'
                        self.current_animation = self.animations[self.state]
                        self.target_position = None
                if event.key == pygame.K_a:
                        self.state = 'attack'
                        self.current_animation = self.animations[self.state]
                        self.current_attack = self.attack_animations['basic_attack']
                        self.target_position = None
   
 
    def calculate_angle(self, position, target_position):
            """ Calculate the angle between the current position and target position """
            direction_vector = target_position - position
            radians = math.atan2(direction_vector.y, direction_vector.x)  # y is inverted in screen space
            angle = math.degrees(radians) % 360  # Convert to degrees and ensure it's in [0, 360)
            angle = (angle+90) % 360
            return angle

