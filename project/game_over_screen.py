import pygame
from config import *

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

pygame.font.init()
default_font = pygame.font.SysFont("Arial", 80, True, False)
return_font = pygame.font.SysFont("Arial", 30, True, False)

def run_game_over_screen(screen, clock):
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return "Quit"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_text_rect.collidepoint(event.pos):
                    return "Menu"
                elif retry_text_rect.collidepoint(event.pos):
                    return "Game"
                
        screen.fill(BLACK)

        game_over_text = default_font.render("You lost...", False, RED)
        return_text = return_font.render("<Return to main menu>", False, YELLOW)
        retry_text = return_font.render("<Retry>", False, WHITE)
        
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 100))
        screen.blit(return_text, (600, 400))
        screen.blit(retry_text, (450, 400))

        return_text_rect = return_text.get_rect(topleft=(600, 400))
        retry_text_rect = retry_text.get_rect(topleft=(450, 400))
        
        pygame.display.flip()
        clock.tick(FPS)

    return "Quit"
            