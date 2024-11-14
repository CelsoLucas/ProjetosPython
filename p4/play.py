import main
import pygame

def play_musica():
    pygame.init()
    pygame.mixer.music.load("ComoVcTa.mp3")
    pygame.mixer.music.play()
    pygame.event.wait()
    input()