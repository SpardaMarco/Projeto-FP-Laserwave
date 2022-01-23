import enemy2
from utils import *

class Spawner2:

    def __init__(self, game):
        self.game = game
        self.enemy_list = self.game.enemy_list
        self.delta = 6
        self.min_spawn_delta = 10
        self.spawn_point = [1580, 200]
        self.final_pos = [1200, 200]
    
    def spawn(self, pos):
        '''Creates an enemy and determine his direction'''
        direction = direction_vector(pos, self.final_pos)

        a = enemy2.Enemy2(self.game, pos, direction, self.final_pos)
        self.enemy_list.append(a)
    
    def check_spawn(self, dt):
        '''Checks if enough time has passed to spawn another round of enemies'''
        for enemy in self.enemy_list:
            if isinstance(enemy, enemy2.Enemy2):
                return
            continue
        self.delta += dt   
        if self.delta >= self.min_spawn_delta:
            self.spawn(self.spawn_point.copy())
            self.delta = 0
        
