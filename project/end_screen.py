import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

pygame.font.init()
default_font = pygame.font.SysFont("Arial", 30, True, False)
rating_font = pygame.font.SysFont("Arial", 60, True, False)

def run_end_screen(screen, clock):
    from game import perfect, good, bad, miss
    rating = " "
    if miss >= 0 and miss <= 10:
        rating = "S"
    elif miss >= 11 and miss <= 15:
        rating = "A"
    elif miss >= 16 and miss <= 20:
        rating = "B"
    elif miss >= 21 and miss <= 25:
        rating = "C"
    elif miss >= 26 and miss <= 30:
        rating = "D"
    else:
        rating = "Failed..."

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return "Quit"
            
        screen.fill(BLACK)
        
        rating_text = rating_font.render("Rating: " + rating, False, CYAN)
        perfect_text = default_font.render("Perfect: " + str(perfect), False, WHITE)
        good_text = default_font.render("Good: " + str(good), False, WHITE)
        bad_text = default_font.render("Bad: " + str(bad), False, WHITE)
        miss_text = default_font.render("Miss: " + str(miss), False, WHITE)

        screen.blit(rating_text, (WIDTH // 2 - 165, HEIGHT // 2))
        screen.blit(perfect_text, (WIDTH // 2 - 75, HEIGHT // 2 + 100))
        screen.blit(good_text, (WIDTH // 2 - 75, HEIGHT // 2 + 150))
        screen.blit(bad_text, (WIDTH // 2 - 75, HEIGHT // 2 + 200))
        screen.blit(miss_text, (WIDTH // 2 - 75, HEIGHT // 2 + 250))

        pygame.display.flip()
        clock.tick(FPS)

    return "Menu"
        
            