import pygame

def background_music():
    pygame.mixer.init()
    #load the music from my files
    pygame.mixer.music.load('battle_music/prepare-to-die-music.mp3')
    #set the volume so it doesnt blast anyones ear drums
    pygame.mixer.music.set_volume(.01)
    # tell it to play continuously
    pygame.mixer.music.play(-1)
    

    
    
