import pygame
import bullet
from utils import *

class Player:

    #Constants
    max_speed = 300
    min_speed = 0.000001

    friction_remainder = 0.33
    gravity_force = 275
    boost_force = 250
    shoot_force = 100
    


    def __init__(self, game) -> None:
        self.game = game
        self.img = pygame.image.load("Entities/Player.png") # Load Player PNG
        self.img.set_colorkey((255,0,255)) # Colorkey
        
        #Position
        self.pos = [640 , 360]
        self.speed = [0 , 0]
        self.size = self.img.get_size()
    

    def draw(self):
        '''Draws himself'''
        self.game.screen.blit(self.img, (self.pos[0] - self.img.get_width()//2 , self.pos[1] - self.img.get_height()//2))

    def move(self, dt):
        
        #Max Speed
        self.speed[0] = min(max(self.speed[0], - self.max_speed), self.max_speed)
        self.speed[1] = min(max(self.speed[1], - self.max_speed), self.max_speed)

        self.pos[0] += self.speed[0]*dt
        self.pos[1] += self.speed[1]*dt
    
    def boost(self):
        mouse_pos = pygame.mouse.get_pos()
        vector = direction_vector(mouse_pos, self.pos)

        if self.speed[0]*vector[0] > 0:
            self.speed[0] += vector[0] * self.boost_force
        else:
            self.speed[0] = vector[0] * self.boost_force

        if self.speed[1]*vector[1] > 0:
            self.speed[1] += vector[1] * self.boost_force
        else:
            self.speed[1] = vector[1] * self.boost_force
        #self.boost_sound.play()
        
    def shoot(self):
        mouse_pos = pygame.mouse.get_pos()
        vector = direction_vector(mouse_pos, self.pos)

        line = bullet.Bullet(self.game, self.pos)
        enemy = None
        for x in self.game.enemy_list:
            if line.check_intersection(x):
                enemy = x
        if enemy != None:
            enemy.enemy_hit()
        
        # Shoot boost
        if self.speed[0]*vector[0] > 0:
            self.speed[0] += vector[0] * self.shoot_force
        else:
            self.speed[0] = vector[0] * self.shoot_force

        if self.speed[1]*vector[1] > 0:
            self.speed[1] += vector[1] * self.shoot_force
        else:
            self.speed[1] = vector[1] * self.shoot_force
        
        return line

        

    
    def physics(self, dt):
        self.speed[1] += self.gravity_force * dt

        if abs(self.speed[0]) < self.min_speed:
            self.speed[0] = 0
        else:
            self.speed[0] -= self.speed[0] * (1 - self.friction_remainder) * dt
    
        if abs(self.speed[1]) < self.min_speed:
            self.speed[1] = 0



    def border_collision(self):
        window_size = self.game.screen.get_size()


        if self.pos[1] > window_size[1] - self.img.get_height(): # Fall of the screen
            self.pos[1] = window_size[1] - self.img.get_height()
            self.speed[1] = - self.speed[1]

        if self.pos[1] < 0 + self.img.get_height(): # Top of the screen
            self.pos[1] = 0 + self.img.get_height()
            self.speed[1] = - self.speed[1]
        
        if self.pos[0] > window_size[0] - self.img.get_width(): # Right of the screen
            self.pos[0] = window_size[0] - self.img.get_width()
            self.speed[0] = - self.speed[0]

        if self.pos[0] < 0 + self.img.get_width(): # Left of the screen
            self.pos[0] = 0 + self.img.get_width()
            self.speed[0] = - self.speed[0]


    def check_intersection(self, rect):
        circle_distance_x = abs(self.pos[0] - rect.pos[0])
        circle_distance_y = abs(self.pos[1] - rect.pos[1])

        if circle_distance_x > (rect.size[0]/2 + self.size[0]/2):
            return False
        if circle_distance_y > (rect.size[1]/2 + self.size[1]/2):
            return False
        
        if circle_distance_x <= rect.size[0]/2:
            return True
        if circle_distance_y <= rect.size[1]/2:
            return True

        corner_distance = (circle_distance_x - rect.size[0]/2 )**2 + (circle_distance_y - rect.size[1]/2 )**2

        return corner_distance <= ((self.size[0]/2)**2)

    def kill(self):
        pass

