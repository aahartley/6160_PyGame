import os
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert_alpha()
    return img

def load_sprite_sheet(path):
    angles = [0, 22, 45, 67, 90, 112, 135, 157, 180, 202, 225, 247, 270, 292, 315, 337]
    sheets = {}
    for angle in angles:
        formatted_angle = f"{angle:03d}"
        sheets[angle] = load_image(path + f"{formatted_angle}.png").convert_alpha()
    return sheets

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name).convert_alpha())
    return images

def scale_image(img, factor):
    w, h = img.get_width() * factor, img.get_height() * factor
    return pygame.transform.scale(img, (int(w), int(h))).convert_alpha()

def sprite_frame_dict(rows, cols, width, height):
    frame_set = {}
    for j in range(rows):
        for i in range(cols):
            x = i % cols * width
            y = j % rows * height
            frame_set[j*cols + i] =  (x, y, width,  height)
    return frame_set

def load_tiles(path):
    tiles = {}
    tiles[0] = load_image(path).convert_alpha()
    tiles[0].set_colorkey((0,0,0))
    tiles[0].set_clip(0,0,256,144)
    tiles[0]=tiles[0].subsurface(tiles[0].get_clip()).convert_alpha()
    return tiles
