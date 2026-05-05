import pygame
from config import *

CYAN = (0, 255, 255)

def isHit(note):
    distance = abs(note.y - Y_HIT_LINE)
    if distance < 25:
        return "Perfect!"
    elif distance < 35 and distance > 25:
        return "Good!"
    elif distance > 35 and distance < 60:
        return "Bad"
    else: 
        return "Miss"

def paused(screen):
    import game
    return_font = pygame.font.SysFont("Arial", 30, True, False)
    dim_layer = pygame.Surface((WIDTH, HEIGHT))
    dim_layer.fill((0, 0, 0))
    dim_layer.set_alpha(128)
    paused_font = pygame.font.SysFont("Arial", 100)
    paused_text_surface = paused_font.render("Paused", False, CYAN)
    return_text = return_font.render("<Return to main menu>", False, YELLOW)
    retry_text = return_font.render("<Retry>", False, WHITE)
    screen.blit(dim_layer, (0, 0))
    screen.blit(paused_text_surface, (500, 284))
    screen.blit(return_text, (600, 400))
    screen.blit(retry_text, (450, 400))
    pygame.display.flip()

    return_text_rect = return_text.get_rect(topleft=(600, 400))
    retry_text_rect = retry_text.get_rect(topleft=(450, 400))

    while game.is_paused:
        pygame.mixer.music.pause()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                game.is_paused = False
                return "Quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.unpause()
                    game.is_paused = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_text_rect.collidepoint(event.pos):
                    game.is_paused = False
                    pygame.mixer.music.unpause()
                    return "Menu"
                elif retry_text_rect.collidepoint(event.pos):
                    game.is_paused = False
                    pygame.mixer.music.unpause()
                    return "Game"
            