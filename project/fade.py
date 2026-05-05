import pygame
from config import *

clock = pygame.time.Clock()

def fade_out(screen, clock, speed = 5):
    fade = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 255)) # 255 means fully opague

    for i in range(0, 256, speed):
        pygame.event.pump() #Keeps window active
        fade.set_alpha(i)
        screen.blit(fade, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

def fade_in(screen, clock, speed = 5):
    fade = pygame.Surface(screen.get_size(), pygame.SRCALPHA)
    fade.fill((0, 0, 0, 255))

    for i in range(255, -1, -speed):
        pygame.event.pump()
        fade.set_alpha(i)
        screen.blit(fade, (0, 0))
        pygame.display.flip()
        clock.tick(FPS)
    


