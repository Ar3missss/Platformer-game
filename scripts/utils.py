import os
import pygame

BASE_IMAGE_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMAGE_PATH + path)): # os.listdir will give you all the images present in the folder like there are 10 images so it will give u all 10 
        images.append(load_image(path + '/' + img_name))
        return images 