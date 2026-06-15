import pygame
import json
from config import *

with open(r"C:\Users\cszel\OneDrive\Documents\GitHub\cs-project\project\charts\songs.json", "r") as f:
    data = json.load(f)
songs = data["songs"]

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

pygame.font.init()
default_font = pygame.font.SysFont("Arial", 30, True, False)
rating_font = pygame.font.SysFont("Arial", 500, True, False)
return_font = pygame.font.SysFont("Arial", 30, True, False)
score_font = pygame.font.SysFont("Arial", 60, True, False)
highest_combo_font = pygame.font.SysFont("Arial", 50, True, True)

def run_end_screen(screen, clock):
    dim_layer = pygame.Surface((WIDTH, HEIGHT))
    dim_layer.fill((0, 0, 0))
    dim_layer.set_alpha(128)

    from leaderboard import Leaderboard, draw_enter_name, draw_leaderboard
    from game import score

    leaderboard = Leaderboard()
    player_name = ""
    entering_name = True

    if score != 0 and leaderboard.is_high_score(score):
        while entering_name:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return "Quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(player_name) > 0:
                        leaderboard.add_score(player_name, score)
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]

            draw_enter_name(score, player_name)

    from game import perfect, good, bad, miss, score, highest_combo
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_text_rect.collidepoint(event.pos):
                    return "Menu"
                elif retry_text_rect.collidepoint(event.pos):
                    return "Game"
            
        screen.fill(BLACK)

        from menu_screen import selected
        bg = pygame.image.load(songs[selected]["background"])
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        screen.blit(bg, bg.get_rect())
        screen.blit(dim_layer, (0, 0))
        
        rating_text = rating_font.render(rating, False, CYAN)
        perfect_text = default_font.render("Perfect: " + str(perfect), False, WHITE)
        good_text = default_font.render("Good: " + str(good), False, WHITE)
        bad_text = default_font.render("Bad: " + str(bad), False, WHITE)
        miss_text = default_font.render("Miss: " + str(miss), False, WHITE)
        return_text = return_font.render("<Return to main menu>", False, YELLOW)
        retry_text = return_font.render("<Retry>", False, WHITE)
        score_text = score_font.render("Score: " + str(score), False, WHITE)
        highest_combo_text = highest_combo_font.render("Max. Combo: " + str(highest_combo), False, GREEN)

        screen.blit(rating_text, (WIDTH // 2 + 200, HEIGHT // 2 - 300))
        screen.blit(perfect_text, (10, HEIGHT // 2 + 100))
        screen.blit(good_text, (10, HEIGHT // 2 + 150))
        screen.blit(bad_text, (10, HEIGHT // 2 + 200))
        screen.blit(miss_text, (10, HEIGHT // 2 + 250))
        screen.blit(return_text, (10, 0))
        screen.blit(retry_text, (10, 50))
        screen.blit(score_text, (10, HEIGHT // 2 - 125))
        screen.blit(highest_combo_text, (10, HEIGHT // 2 - 65))

        return_text_rect = return_text.get_rect(topleft=(10, 0))
        retry_text_rect = retry_text.get_rect(topleft=(10, 50))

        draw_leaderboard(leaderboard)

        pygame.display.flip()
        clock.tick(FPS)

        
            