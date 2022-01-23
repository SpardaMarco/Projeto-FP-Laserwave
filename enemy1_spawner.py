import enemy1
from utils import *

class Spawner:

    def __init__(self, game):
        self.game = game
        self.enemy_list = game.enemy_list
        self.delta = 6
        self.min_spawn_delta = 10
        self.spawn_points = [[0, 0], [640, 0], [0, 720], [640, 720]]
    
    def spawn(self, pos):
        '''Creates an enemy and determine his direction'''
        direction = direction_vector(pos, self.game.player.pos)

        a = enemy1.Enemy1(self.game, pos, direction)
        self.enemy_list.append(a)
    
    def check_spawn(self, dt):
        '''Checks if enough time has passed to spawn another round of enemies'''
        self.delta += dt
        if self.delta >= self.min_spawn_delta:
            for i in self.spawn_points:
                self.spawn(i.copy())
            self.delta = 0
        
