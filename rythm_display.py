import pygame

class RythmDisplay:
    def __init__(self, game):
        self.game = game
        self.pos = [640, 654]
        self.size = [100, 16]

    def draw(self):
        '''Draws himself'''
        sm = self.game.sound_manager
        width_percent = sm.rythym[sm.counter] - sm.dt
        size = [self.size[0]*width_percent, self.size[1]]

        position = [self.pos[0]-size[0]/2, self.pos[1]-size[1]/2]

        if sm.soundsOrder[sm.counter] == 0:
            color = (200,0,0)
        else:
            color = (0,0,200)

        body = pygame.Rect(position, size)
        pygame.draw.rect(self.game.screen, color, body)