import pygame
import enemy1_spawner
from utils import *


class Enemy2:
    class False_Body:
        def __init__(self, parent): # Init Function
            #set variables
            self.parent = parent
            self.pos = parent.pos.copy()
            self.pos[1] += 200
            self.enemy_list = parent.enemy_list
            self.size = (300, 300)
            self.speed = 60
            self.direction = [parent.direction[0], parent.direction[1] + 200]
            self.enemy1_spawner = enemy1_spawner.Spawner(self.parent.game)
            self.enemy1_spawner.spawn_points = [[self.pos[0], self.pos[1]-50], [self.pos[0], self.pos[1]+50]]
        
        def draw(self):
            '''Draws himself'''
            false_position = [self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2 ]
            false_body = pygame.Rect(false_position, self.size)
            pygame.draw.rect(self.parent.game.screen, (64,43,94), false_body)


        def move(self):
            '''Updates self.pos'''
            self.pos[0] = self.parent.pos[0]
            self.pos[1] = self.parent.pos[1] + 200
            self.enemy1_spawner.spawn_points = [[self.pos[0], self.pos[1]-50], [self.pos[0], self.pos[1]+50]]

        def corners(self):
            top_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
            top_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
            bottom_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)
            bottom_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)

            return (top_left, top_right, bottom_right, bottom_left)
    
    def __init__(self, game, spawn_pos, direction, final_pos): # Init Function
        #set variables
        self.game = game
        self.pos = spawn_pos
        self.size = (300, 300)
        self.speed = 100
        self.enemy_list = self.game.enemy_list

        self.direction = direction
        self.counter = 0
        self.final_pos = final_pos
        self.false_body = self.False_Body(self)
        self.has_false_body = True

    
    def draw(self):
        '''Draws himself'''
        position = [self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2 ]
        body = pygame.Rect(position, self.size)
        self.false_body.draw()
        pygame.draw.rect(self.game.screen, (130,69,195), body)

    def move(self, dt):
        '''Updates self.pos'''

        self.pos[0] += self.direction[0] * self.speed * dt
        self.pos[1] += self.direction[1] * self.speed * dt
        if self.pos[0] <= self.final_pos[0]:
            self.pos = self.final_pos.copy()
        print(self.pos)
        print(self.final_pos)
        self.false_body.move()

        

    def enemy_hit(self):
        self.counter += 1
        if self.counter >= 3:
            self.game.enemy_list.remove(self)

    def corners(self):
        top_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
        top_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]-self.size[1]*0.5)
        bottom_right = (self.pos[0]+self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)
        bottom_left = (self.pos[0]-self.size[0]*0.5, self.pos[1]+self.size[1]*0.5)

        return (top_left, top_right, bottom_right, bottom_left)


