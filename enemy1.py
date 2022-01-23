import pygame
from utils import *


class Enemy1:

    def __init__(self, game, spawn_pos, direction): # Init Function
        #set variables
        self.game = game
        self.pos = spawn_pos
        self.size = (48, 48)
        self.speed = 60
        self.direction = direction
        self.has_false_body = False
    
    def draw(self):
        '''Draws himself'''
        position = [self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2 ]
        body = pygame.Rect(position, self.size)
        pygame.draw.rect(self.game.screen, (130,50,254), body)

    def move(self, dt):
        '''Updates self.pos'''
        self.pos[0] += self.direction[0] * self.speed * dt
        self.pos[1] += self.direction[1] * self.speed * dt

    def enemy_hit(self):
        self.game.enemy_list.remove(self)

    def corners(self):
        top_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
        top_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
        bottom_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)
        bottom_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)

        return (top_left, top_right, bottom_right, bottom_left)


