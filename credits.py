import pygame

class Credits:
    #Constants
    background_color = (17, 23, 31)


    def __init__(self, screen, state_machine, my_font, credits_font):
        self.screen = screen
        self.state_machine = state_machine
        self.my_font = my_font
        self.credits_font = credits_font

    def gameloop(self, dt_sec):
        '''Checks for inputs'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.state_machine.event_all_to_quit()
            elif event.type == pygame.KEYDOWN: # KeyPressed
                if event.key == pygame.K_SPACE:
                    self.state_machine.event_credits_to_menu()


        self.screen.fill(self.background_color)
        
        #Text

        text_surface = self.my_font.render("Thanks for playing", False, (254,254,70))
        credits_1_surface = self.credits_font.render("Made for PROJ FP 2021/2022 by Marco Costa", False, (254,254,70))
        credits_2_surface = self.credits_font.render("Music:", False, (254,254,70))
        credits_3_surface = self.credits_font.render("'Synthwavey Chords' by calebclarkmusic (Looperman)", False, (254,254,70))
        credits_4_surface = self.credits_font.render("'Synthwave Bass Synth' by SimonInvader (Looperman)", False, (254,254,70))
        credits_5_surface = self.credits_font.render("SFX from FreeSounds", False, (254,254,70))
        self.screen.blit(text_surface,(self.screen.get_width()/2- text_surface.get_width()/2,100))
        self.screen.blit(credits_1_surface,(self.screen.get_width()/2- credits_1_surface.get_width()/2,200))
        self.screen.blit(credits_2_surface,(self.screen.get_width()/2- credits_2_surface.get_width()/2,300))
        self.screen.blit(credits_3_surface,(self.screen.get_width()/2- credits_3_surface.get_width()/2,400))
        self.screen.blit(credits_4_surface,(self.screen.get_width()/2- credits_4_surface.get_width()/2,500))
        self.screen.blit(credits_5_surface,(self.screen.get_width()/2- credits_5_surface.get_width()/2,600))

        
    