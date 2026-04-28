import pygame
from config import *

CYAN = (0, 255, 255)

def isHit(note):
    distance = abs(note.y - Y_HIT_LINE)
    if distance < 15:
        return "Perfect!"
    elif distance < 30 and distance > 15:
        return "Good!"
    elif distance > 30 and distance < 60:
        return "Bad"
    else: 
        return "Miss"

def paused(screen):
    import game
    paused_font = pygame.font.SysFont("Arial", 100)
    paused_text_surface = paused_font.render("Paused", False, CYAN)
    screen.blit(paused_text_surface, (500, 284))
    pygame.display.flip()

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
            