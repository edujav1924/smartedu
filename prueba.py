
import pygame
import time
pygame.mixer.pre_init(23050, -16, 2, 1024) # setup mixer to avoid sound lag

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load('apagado.mp3')

pygame.mixer.music.play()
time.sleep(4)
