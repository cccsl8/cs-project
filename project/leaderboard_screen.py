import pygame
from config import *
from leaderboard import *

leaderboard = Leaderboard()

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

default_font = pygame.font.SysFont("Arial", 30, True, False)
large_font = pygame.font.SysFont("Arial", 50, True, False)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(BLACK)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()