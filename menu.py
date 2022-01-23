import pygame

class Menu:
    #Constants
    background_color = (17, 23, 31)


    def __init__(self, screen, state_machine, my_font, credits_font) -> None:
        self.screen = screen
        self.state_machine = state_machine
        self.my_font = my_font
        self.credits_font = credits_font

    def gameloop(self, dt_sec):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.event_all_to_quit()
            elif event.type == pygame.KEYDOWN: # KeyPressed
                if event.key == pygame.K_SPACE:
                    self.state_machine.event_menu_to_game()
                elif event.key == pygame.K_TAB:
                    self.state_machine.event_menu_to_credits()

        self.screen.fill(self.background_color)

        text_surface = self.my_font.render("Press SPACE to start", False, (254,254,70))
        credits_surface = self.credits_font.render("Press TAB to see Credits", False, (254,254,70))
        self.screen.blit(text_surface,(self.screen.get_width()/2- text_surface.get_width()/2,300))
        self.screen.blit(credits_surface,(self.screen.get_width()/2- credits_surface.get_width()/2,500))
    