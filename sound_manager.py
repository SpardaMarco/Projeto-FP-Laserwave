import pygame

pygame.mixer.init()

class Sound:
    def __init__(self) -> None:
        
        self.game_music = "assets/sound/SynthwaveBassSynth.wav"
        self.menu_music = "assets/sound/SynthwaveyChords.wav"
        self.bullet_sound = pygame.mixer.Sound("assets/sound/Clap.wav")
        self.boost_sound = pygame.mixer.Sound("assets/sound/DrumBeat.wav")
        self.counter = 0
        self.dt = 0

        self.rythym = [0.706, 0.706, 0.706, 0.706, 0.706, 0.706, 0.353, 0.353, 0.706, 0.706, 0.706, 0.706, 0.706, 0.176, 0.176, 0.353, 0.353, 0.176, 0.353, 0.353, 0.176, 0.353, 0.353]
        self.soundsOrder = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1]

    
    def play_game_music(self):
        pygame.mixer.music.load(self.game_music)
        pygame.mixer.music.play(-1)
    
    def play_menu_music(self):
        pygame.mixer.music.load(self.menu_music)
        pygame.mixer.music.play(-1)

    def play_bullet_sound(self):
        self.bullet_sound.play()
    
    def play_boost_sound(self):
        self.boost_sound.play()

    def reset(self):
        self.counter = 0
        self.dt = 0

    def check_event(self, dt_sec):
        self.dt += dt_sec
        
        if self.dt >= self.rythym[self.counter]:
            sound = self.soundsOrder[self.counter]
            self.dt -= self.rythym[self.counter]
            self.counter += 1
            if self.counter >= len(self.rythym):
                self.counter = 0
            return sound
        return None
        
        


