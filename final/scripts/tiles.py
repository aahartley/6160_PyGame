import pygame
from scripts.utils import load_image, load_images, sprite_frame_dict, load_sprite_sheet, load_tiles
import math

class Tile:
    def __init__(self, width, height):
        self.tiles = load_tiles("tiles/Overworld-Large/Thick/Overworld-Terrain1-Thick256x144.png",6, 3, 256, 144)
        self.screen_width = width
        self.screen_height = height
        self.tile_width = 256
        self.tile_height = 144
        self.tile_map = [ #17
            [0, 1, 2, 3, 4],
            [5, 6, 7, 8, 9],
            [10, 11, 12, 13, 14],
            [15, 16, 17, 0, 1],
            [2, 3, 4, 5, 6]
        ]

    def draw(self, screen):
        x_start = self.screen_width//2 - self.tile_width//2
        y_start = -self.tile_height*2
        #y_start = 0
        extra= 5  #5
        offset = 0 #8
        for j in range(0,self.screen_height//self.tile_height+extra):
            for i in range(0,self.screen_width//self.tile_width+extra):
                x_screen = x_start+(i-j)*(self.tile_width//2)
                y_screen = y_start + (i+j)*(self.tile_height//2-offset)
                screen.blit(self.tiles[1], (x_screen, y_screen))


        # for j, row in enumerate(self.tile_map):
        #     for i, tile_id in enumerate(row):
        #         x_screen = x_start+(i-j)*(self.tile_width//2)
        #         y_screen = y_start + (i+j)*(self.tile_height//2-offset)
        #         screen.blit(self.tiles[tile_id], (x_screen, y_screen))
        #         #pygame.draw.rect(screen, (255,0,0), (i*self.tile_width, j*self.tile_height, self.tile_width, self.screen_height), 1)