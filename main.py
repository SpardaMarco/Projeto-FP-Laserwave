import pygame
import game
import menu
import credits
import sound_manager

class State_Machine:
    def __init__(self) -> None:
        self.state = "Menu"
        self.sound_manager = sound_manager.Sound()
        self.sound_manager.play_menu_music()
        self.game_instance = game.Game(screen, self)
        self.menu_instance = menu.Menu(screen, self, menu_font, credits_font)
        self.credits_instance = credits.Credits(screen, self, menu_font, credits_font)
        self.passed_time = 0
        self.timer_started = False


    
    def event_all_to_quit(self):
        self.state = "Quit"
    
    def event_menu_to_game(self):
        self.game_instance = game.Game(screen, self)
        self.start_time = pygame.time.get_ticks()
        self.timer_started = True
        self.state = "Game"
        self.sound_manager.play_game_music()
    
    def event_game_to_menu(self):
        self.state = "Menu"
        self.timer_started = False
        self.sound_manager.play_menu_music()
    
    def event_credits_to_menu(self):
        self.state = "Menu"
    
    def event_menu_to_credits(self):
        self.state = "Credits"




#Init
clock = pygame.time.Clock()
pygame.init()


pygame.font.init() 
menu_font = pygame.font.Font("assets/fonts/Shockwave.ttf", 50)
credits_font = pygame.font.SysFont("Comic Sans MS", 30)




#Flags
gameloop = True

window_size = (1280, 720) #Game Canvas Size
screen = pygame.display.set_mode(window_size) # Initiate the window

pygame.display.set_caption("Laserwave")
icon = pygame.image.load('Entities/Player.png')
pygame.display.set_icon(icon)

state_machine = State_Machine()





while gameloop:
    dt = clock.tick(60)
    dt_sec = dt/1000

    
    if state_machine.state == "Menu":
        state_machine.menu_instance.gameloop(dt_sec)
    elif state_machine.state == "Game":
        state_machine.game_instance.gameloop(dt_sec)
    elif state_machine.state == "Credits":
        state_machine.credits_instance.gameloop(dt_sec)
    elif state_machine.state == "Quit":
        break
    if state_machine.timer_started:
        state_machine.passed_time = pygame.time.get_ticks() - state_machine.start_time

    timer_surface = menu_font.render(str(state_machine.passed_time/1000), False, (254,254,70))
    screen.blit(timer_surface, (screen.get_width()/2- timer_surface.get_width()/2,50))

    pygame.display.update()


pygame.quit()