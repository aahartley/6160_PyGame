import pygame
from scripts.utils import load_image, load_images, sprite_frame_dict, load_sprite_sheet
import math

class Character(pygame.sprite.Sprite):
    
 
    def __init__(self, position):
        super().__init__()
        self.sheets = load_sprite_sheet("x320p_Spritesheets/Walk_Armed/Walk_Armed_Body_")
        self.shadow_sheets = load_sprite_sheet("x320p_Spritesheets/Walk_Armed/Walk_Armed_Shadow_")
        self.active_sheet = self.sheets[0]
        self.active_sheet.set_clip(pygame.Rect(0, 0, 320, 320)) 
        self.image = self.active_sheet.subsurface(self.active_sheet.get_clip())
        self.rect = self.image.get_rect()
        self.active_shadow_sheet = self.shadow_sheets[0]
        self.active_shadow_sheet.set_clip(pygame.Rect(0,0,320,320))
        self.shadow_image = self.active_shadow_sheet.subsurface(self.active_shadow_sheet.get_clip())
        self.position = pygame.Vector2(position)
        self.rect.topleft = position
        self.frame = 0
        self.rectWidth = 320
        self.rectHeight = 320
        self.walk_000 =  sprite_frame_dict(4, 5, 320, 320)
        self.walk_022 = sprite_frame_dict(4,5,320,320)
        self.speed = 200
        self.time = 0
        self.idle = True
        self.target_position = None
        self.right_click_held = False
        

    def get_frame(self, frame_set):
        if(self.time >= 1/60 ):
            if self.frame+1 > (len(frame_set) - 1):
                self.frame = 0
            else:
                self.frame += 1
            self.time = 0

       
        return frame_set[self.frame]


        
    def clip(self, clipped_rect):
        #If clipped_rect is a dictionary (a frame set),
        if type(clipped_rect) is dict:
            self.active_sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
            self.active_shadow_sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.active_sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
    def update(self, dt):
        # Determine the angle and get the corresponding frame set
        # if self.target_position:
        #     self.time += dt
        #     angle = self.calculate_angle(self.position, self.target_position)
        #     self.get_angle_based_frame_set(angle)
        #     self.clip(self.walk_000)

        self.image = self.active_sheet.subsurface(self.active_sheet.get_clip())
        self.shadow_image = self.active_shadow_sheet.subsurface(self.active_shadow_sheet.get_clip())
        self.rect = self.image.get_rect()

        if self.target_position:
                direction_vector = self.target_position - self.position
                #print(direction_vector)
                if direction_vector.length() > 0:  # Check if the vector is non-zero
                    self.time += dt
                    angle = self.calculate_angle(self.position, self.target_position)
                    self.get_angle_based_frame_set(angle)
                    self.clip(self.walk_000)
                    direction = direction_vector.normalize()  # Get the direction
                    distance_to_move = self.speed * dt  # Distance to move in this frame
                    distance_to_target = self.position.distance_to(self.target_position)

                    # If close enough, stop moving
                    if distance_to_move >= distance_to_target:
                        self.position = self.target_position
                        self.target_position = None  # Stop movement when the target is reached
                    else:
                        self.position += direction * distance_to_move

        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]-50
    
    def draw(self, screen):
        screen.blit(self.shadow_image, self.rect)
        topleft = self.rect.topleft
        screen.blit(self.image, (topleft[0]-1, topleft[1]+25))



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
            

   
 
    def calculate_angle(self, position, target_position):
            """ Calculate the angle between the current position and target position """
            direction_vector = target_position - position
            radians = math.atan2(direction_vector.y, direction_vector.x)  # y is inverted in screen space
            angle = math.degrees(radians) % 360  # Convert to degrees and ensure it's in [0, 360)
            angle = (angle+90) % 360
            return angle

    def get_angle_based_frame_set(self, angle):
        """ Get the frame set based on the current angle """
        # Find the closest matching angle in your defined angles
        available_angles = list(self.sheets.keys())
        closest_angle = min(available_angles, key=lambda x: abs(x - angle))
        self.active_sheet = self.sheets[closest_angle]
        self.active_shadow_sheet = self.shadow_sheets[closest_angle]
