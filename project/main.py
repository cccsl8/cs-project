# USE PYTHON 3.12 (64-BIT)

import pygame
from config import *
from fade import *
from title_screen import run_title_screen
from game import run_game
from menu_screen import run_menu_screen
from loading_screen import run_loading_screen
from end_screen import run_end_screen
from game_over_screen import run_game_over_screen

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()

    current_screen = "Title"
    while True:
        if current_screen == "Title":
            next_screen = run_title_screen(screen, clock)
            fade_out(screen, clock)
        elif current_screen == "Game":
            fade_in(screen, clock)
            next_screen = run_game(screen, clock)
            fade_out(screen, clock)
        elif current_screen == "Menu":
            fade_in(screen, clock)
            next_screen = run_menu_screen(screen, clock)
            fade_out(screen, clock)
        elif current_screen == "Loading":
            fade_in(screen, clock)
            next_screen = run_loading_screen(screen, clock)
            fade_out(screen, clock)
        elif current_screen == "End":
            fade_in(screen, clock)
            next_screen = run_end_screen(screen, clock)
            fade_out(screen, clock)
        elif current_screen == "GameOver":
            fade_in(screen, clock)
            next_screen = run_game_over_screen(screen, clock)
            fade_out(screen, clock)
        else:
            break

        if next_screen == "Quit":
            break
        current_screen = next_screen

    pygame.quit()

main()