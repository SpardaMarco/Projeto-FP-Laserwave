import pygame
from utils import *


class Bullet:

    color = (254,254,70)
    width = 3



    def __init__(self, game, start):
        self.game = game
        self.delta = 0
        self.lifetime = 0.2
        start = start.copy()
        mouse_pos = pygame.mouse.get_pos()
        direction = direction_vector(start, mouse_pos)
        end = [start[0]+ direction[0]*10000, start[1]+ direction[1]*10000]

        self.coordinates = [start, end]

    def draw(self):
        '''Draws himself'''

        pygame.draw.line(self.game.screen, self.color, self.coordinates[0], self.coordinates[1], self.width)
        
    
    def check_intersection(self, rect):
        '''Check intersection between Line and Rect. Edits line coordinates to the shortest line with collision'''
        corners = rect.corners()
        top_line = (corners[0], corners[1])
        right_line = (corners[1], corners[2])
        bottom_line = (corners[2], corners[3])
        left_line = (corners[3], corners[0])

        top_intersect = line_intersection(self.coordinates, top_line)
        right_intersect = line_intersection(self.coordinates, right_line)
        bottom_intersect = line_intersection(self.coordinates, bottom_line)
        left_intersect = line_intersection(self.coordinates, left_line)

        intersects_list =  [top_intersect, right_intersect, bottom_intersect, left_intersect]
        end = None
        end_distance = 100000000000000
        
        for x in intersects_list:
            if x != None:
                dis = distance(self.coordinates[0], x)
                if dis < end_distance:
                    end_distance = dis
                    end = x
        if end == None:
            return False
        
        self.coordinates[1] = end

        return True
        
    def check_bullet(self, dt):
        '''Delete Bullet'''
        self.delta += dt
        if self.delta >= self.lifetime:
            return True