import pygame
import time

EMPTY = 0
WALL = 1
POINT = 2
CHECKED = 2

class Block():
    def __init__(self,code=EMPTY):
        self.code = code
        self.path = ""

def main():
    
    pygame.init()
    window = pygame.display.set_mode((800,600))
    
    