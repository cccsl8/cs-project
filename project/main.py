# USE PYTHON 3.12 (64-BIT)

import pygame
from config import *
from title_screen import run_title_screen
from game import run_game
from menu_screen import run_menu_screen
from loading_screen import run_loading_screen
from end_screen import run_end_screen

def main():
    pygame.init()
    pygame.mixer.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    clock = pygame.time.Clock()

    current_screen = "Title"
    while True:
        if current_screen == "Title":
            next_screen = run_title_screen(screen, clock)
        elif current_screen == "Game":
            next_screen = run_game(screen, clock)
        elif current_screen == "Menu":
            next_screen = run_menu_screen(screen, clock)
        elif current_screen == "Loading":
            next_screen = run_loading_screen(screen, clock)
        elif current_screen == "End":
            next_screen = run_end_screen(screen, clock)
        else:
            break

        if next_screen == "Quit":
            break
        current_screen = next_screen

    pygame.quit()

main()