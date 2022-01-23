import pygame
from utils import *
import player
import enemy1_spawner
import enemy2_spawner
import rythm_display


class Game:
    #Constants
    background_color = (17, 23, 31)
    def __init__(self, screen, state_machine) -> None:
        self.enemy_list = [] # List of enemies
        self.bullet_list = []
        self.screen = screen
        self.state_machine = state_machine
        self.sound_manager = state_machine.sound_manager
        self.sound_manager.reset()
        self.rythm_display = rythm_display.RythmDisplay(self)
        self.player = player.Player(self)
        self.enemy1_spawner = enemy1_spawner.Spawner(self)
        self.enemy2_spawner = enemy2_spawner.Spawner2(self)
        


    def gameloop(self, dt_sec):
        #Flags
        mouse_event = False
        shoot_event = False

        #1. Input events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.event_all_to_quit()
        
        sound_event = self.sound_manager.check_event(dt_sec) 
        if sound_event == 0:
            mouse_event = True
        elif sound_event == 1:
            shoot_event = True


        #2. Game logic and physics
        self.player.physics(dt_sec)
        
        if mouse_event: # Boost
            mouse_event = False
            self.sound_manager.play_boost_sound()
            self.player.boost()
            
        
        if shoot_event:
            shoot_event = False
            self.sound_manager.play_bullet_sound()
            self.bullet_list.append(self.player.shoot())
           




        self.player.move(dt_sec)
        self.player.border_collision()

        self.enemy1_spawner.check_spawn(dt_sec)
        self.enemy2_spawner.check_spawn(dt_sec)
        for enemy in self.enemy_list:
            if enemy.has_false_body:
                enemy.false_body.enemy1_spawner.check_spawn(dt_sec)
    
        


        # Enemy Movement
        for enemy in self.enemy_list:
            enemy.move(dt_sec)
            if self.player.check_intersection(enemy):
                self.state_machine.event_game_to_menu()
            if enemy.has_false_body:
                if self.player.check_intersection(enemy.false_body):
                    self.state_machine.event_game_to_menu()

            
        
        for bullet in self.bullet_list:
            if bullet.check_bullet(dt_sec):
                self.bullet_list.remove(bullet)

        #3. Canvas editing
        self.screen.fill(self.background_color)
        self.player.draw()

        pygame.draw.rect(self.screen, (70,28,40, 1), (0, 0, self.player.img.get_width()/2, self.screen.get_height())) # Left Wall
        pygame.draw.rect(self.screen, (70,28,40, 1), (0, 0, self.screen.get_width(), self.player.img.get_height()/2)) # Top Wall
        pygame.draw.rect(self.screen, (70,28,40, 1), (self.screen.get_width()-self.player.img.get_width()/2, 0, self.player.img.get_width()/2, self.screen.get_height())) # Right Wall
        pygame.draw.rect(self.screen, (70,28,40, 1), (0, self.screen.get_height()-self.player.img.get_height()/2, self.screen.get_width(), self.player.img.get_height()/2)) # Left Wall


        for enemy in self.enemy_list:
            enemy.draw()

        for bullet in self.bullet_list:
            bullet.draw()

        self.rythm_display.draw()



