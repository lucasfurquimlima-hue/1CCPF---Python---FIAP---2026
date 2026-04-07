import pygame

pygame.mixer.init()
pygame.mixer_music.load("Mcpoze.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()

import playsound
playsound("Mcpoze.mp3")
