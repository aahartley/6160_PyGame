import pygame
import scripts.utils as utils
import math
import scripts.animations as ani
import scripts.projectiles as proj
class Character(pygame.sprite.Sprite):
    
 
    def __init__(self, position, scale):
        super().__init__()

        self.animations = {
            'idle': ani.Animation(utils.player_paths[0], utils.player_shadow_paths[0], utils.sprite_frame_dict(4, 4, 320, 320), 30, False, 0),
            'walk': ani.Animation(utils.player_paths[1], utils.player_shadow_paths[1], utils.sprite_frame_dict(4, 6, 320, 320), 60, False, 0),
            'attack': ani.Animation(utils.player_paths[2],utils.player_shadow_paths[2], utils.sprite_frame_dict(4, 6, 320, 320), 60, False, 0)#100
        }
        self.attack_animations = {
            #'basic_arrow_attack': ani.Animation(utils.prop_paths[0], utils.prop_paths[0],utils.sprite_frame_dict(1,1,1024,1024), 60, True, 0.20),
            'basic_arrow_attack': utils.scale_image(utils.load_image("Props/1024x1024/Arrow_Far/Arrow_Far_000.png").convert_alpha(), 0.2)

        }
        self.projectiles = []
        self.current_animation = self.animations['idle']
        self.image, self.shadow_image = self.current_animation.get_current_frames()
        self.position = pygame.Vector2(position) 
        self.speed = 200
        self.target_position = None
        self.right_click_held = False
        self.state = 'idle'     
        self.angle = 0
        self.real_angle = 90
        self.drawing_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_bounding_rects()[0]
        # self.rect.centerx = position[0]
        # self.rect.centery = position[1]
        self.rect.centerx = self.position[0]
        self.rect.centery = self.position[1]       
        self.local_centroid = pygame.Vector2(self.mask.centroid())
        self.bow_pos = pygame.Vector2(self.local_centroid)
        self.bow_pos[0] += 20  # Offset for the bow's position in local space (relative to the body)
        self.bow_pos[1] -= 150  # Adjust as needed to match the sprite's local position
        self.bow_world = pygame.Vector2(self.drawing_rect.x + self.bow_pos[0], self.drawing_rect.y + self.bow_pos[1])

    def change_state(self, state, reset):
        if reset:
            self.animations[self.state].reset()
        self.state = state
        self.current_animation = self.animations[self.state]

    def update(self, dt):
        for p in self.projectiles:
            p.update(dt)
        self.projectiles = [p for p in self.projectiles if not p.hit]

        if self.state == 'attack':
            if(self.current_animation.frame >=15):
                if len(self.projectiles) > 0:
                    self.projectiles[-1].fire = True
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
        for p in self.projectiles:
            p.draw(screen)
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

        pygame.draw.circle(screen, (0, 255, 0), (self.drawing_rect.x + self.bow_pos[0], self.drawing_rect.y + self.bow_pos[1]), 2)



            #pygame.draw.line(screen, (0, 255, 0), p.position, p.target_position)

        # pygame.draw.circle(screen, (255, 0, 0), self.position, 3) 
        #pygame.draw.circle(screen, (0, 255, 0), (self.drawing_rect.x + self.local_centroid[0], self.drawing_rect.y + self.local_centroid[1]-30), 3)

        #pygame.draw.circle(screen, (0, 255, 0), (drawing_rect.x + bow_pos[0], drawing_rect.y + bow_pos[1]), 2)

    




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
                        self.change_state('idle', True)
                        self.target_position = None
                if event.key == pygame.K_a:
                        if self.state != 'attack':
                            mouse_pos = pygame.mouse.get_pos()
                            self.angle = self.calculate_angle(pygame.Vector2(self.rect.center), mouse_pos)
                            self.real_angle = self.calc_real_angle(pygame.Vector2(self.rect.center), mouse_pos)
                            #print(self.angle)
                            #print(self.real_angle)
                             # Get the local position of the bow relative to the archer's body
                            self.bow_pos = pygame.Vector2(self.local_centroid)
                            self.bow_pos[0] += 20  # Offset for the bow's position in local space (relative to the body)
                            self.bow_pos[1] -= 150  # Adjust as needed to match the sprite's local position

                            # Convert to the available angle range used by the animation
                            available_angles = list(self.current_animation.sheets.keys())
                            closest_angle = min(available_angles, key=lambda x: abs(x - self.real_angle))
                            #closest_angle = self.real_angle
                            # Store original bow position to use in rotation calculation
                            bow_local_x = self.bow_pos[0] - self.local_centroid[0]
                            bow_local_y = self.bow_pos[1] - self.local_centroid[1]-10

                            # Rotate the bow position by the closest angle
                            rotated_bow_x = math.cos(math.radians(closest_angle)) * bow_local_x - math.sin(math.radians(closest_angle)) * bow_local_y
                            rotated_bow_y = math.sin(math.radians(closest_angle)) * bow_local_x + math.cos(math.radians(closest_angle)) * bow_local_y

                            # Add back the local centroid to position the bow in world space
                            self.bow_pos[0] = rotated_bow_x + self.local_centroid[0]
                            self.bow_pos[1] = rotated_bow_y + self.local_centroid[1]-10

                            # Drawing bow position (convert to screen coordinates)
                            self.bow_world = pygame.Vector2(self.drawing_rect.x + self.bow_pos[0], self.drawing_rect.y + self.bow_pos[1])
                            #self.projectiles.append(proj.Projectile(self.attack_animations['basic_arrow_attack'].copy(), pygame.Vector2(self.rect.center), mouse_pos, self.bow_world))
                            test = pygame.Vector2((self.drawing_rect.x + self.local_centroid[0], self.drawing_rect.y + self.local_centroid[1]-30))
                            self.projectiles.append(proj.Projectile(self.attack_animations['basic_arrow_attack'].copy(), pygame.Vector2(test), mouse_pos, self.bow_world))

                        self.change_state('attack', False)
                        self.target_position = None

 
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

