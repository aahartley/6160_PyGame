import pygame
from scripts.utils import load_image, load_images, sprite_frame_dict, load_sprite_sheet, load_tiles
import math

class Tile:
    def __init__(self, width, height):
        self.tiles = load_tiles("tiles/Overworld-Large/Thick/Overworld-Terrain1-Thick256x144.png")
        self.screen_width = width
        self.screen_height = height
        self.tile_width = 256
        self.tile_height = 144

    def draw(self, screen):
        x_start = self.screen_width//2 - self.tile_width//2
        y_start = -self.tile_height*2
        extra= 5
        for j in range(0,self.screen_height//self.tile_height+extra):
            for i in range(0,self.screen_width//self.tile_width+extra):
                x_screen = x_start+(i-j)*(self.tile_width//2)
                y_screen = y_start + (i+j)*(self.tile_height//2-8)
                screen.blit(self.tiles[0], (x_screen, y_screen))