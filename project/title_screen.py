import pygame
import gif_pygame as gp
from config import *

TITLE_MUSIC = r"C:\Users\cszel\OneDrive\Documents\GitHub\chansz-python\menu_theme.mp3"

def run_title_screen(screen, clock):
    pygame.font.init()
    default_font = pygame.font.SysFont("Comic Sans MS", 50, True)
    pygame.mixer.music.load(TITLE_MUSIC)
    pygame.mixer.music.play(-1)
    animation1 = gp.load("title background 1.gif")
    animation2 = gp.load("title background 2.gif")
    animation3 = gp.load("title background 3.gif")

    #dim the background gifs
    dim_layer = pygame.Surface((WIDTH, HEIGHT))
    dim_layer.fill((0, 0, 0))
    dim_layer.set_alpha(128)

    start_text_font = pygame.font.SysFont("Arial", 30, True)

    start_time = pygame.time.get_ticks()

    running = True
    while running:
        time_passed = pygame.time.get_ticks() - start_time
        if time_passed < 5000:
            current_animation = animation1
        elif time_passed < 10000:
            current_animation = animation2
        else:
            current_animation = animation3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("clicked menu")
                    return "Menu"

        screen.fill(BLACK)
        current_animation.render(screen, (0, 0))
        screen.blit(dim_layer, (0, 0))

        menu_text = "DRUM HERO"
        menu_text_surface = default_font.render(menu_text, False, CYAN)
        screen.blit(menu_text_surface, (500, 331))

        start_text = "Press Space to start"
        start_text_surface = start_text_font.render(start_text, False, WHITE)
        screen.blit(start_text_surface, (490, 426))

        pygame.display.flip()
        clock.tick(FPS)
