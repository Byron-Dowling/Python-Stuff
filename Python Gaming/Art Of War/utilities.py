import pygame

def background_music():
    pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('battle_music\prepare-to-die-music.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(.01)
    # tell it to play continuously
    pygame.mixer.music.play(-1)
    
def fight_sound_1():
    pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('fight_sounds/sword-slide-fight.wav')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.3)
    # tell it to play once
    pygame.mixer.music.play(0)
    
def fight_sound_2():
    # pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('fight_sounds/sword-cutt-flesh.wav')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.3)
    # tell it to play once
    pygame.mixer.music.play(0)
    
def fight_sound_3():
    # pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('fight_sounds/knife-slice-cut.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.3)
    # tell it to play once
    pygame.mixer.music.play(0)
    
def fight_sound_4():
    # pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('fight_sounds/body-cut-impact.wav')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.3)
    # tell it to play once
    pygame.mixer.music.play(0)
    
def win_sound():
    # pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('fight_sounds/eren-titan-roar.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(0.1)
    # tell it to play once
    pygame.mixer.music.play(0)
    
    
