import pygame
from config import *

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

title_font = pygame.font.SysFont("Arial", 50, True, False)
setting_font = pygame.font.SysFont("microsoftsansserif", 30, False, False)

running = True
while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        
    screen.fill(BLACK)

    title = title_font.render("Settings:", False, WHITE)
    screen.blit(title, (10, 10))

    scroll_speed_text = setting_font.render("Scroll speed:" , False, WHITE)
    screen.blit(scroll_speed_text, (10, 100))

    note_colour_text = setting_font.render("Note colour:", False, WHITE)
    screen.blit(note_colour_text, (10, 175))

    keybind_text = setting_font.render("Keybinds:", False, WHITE)
    screen.blit(keybind_text, (10, 250))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()