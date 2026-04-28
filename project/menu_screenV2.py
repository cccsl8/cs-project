import pygame
from config import *
import json

with open(r"C:\Users\cszel\OneDrive\Documents\GitHub\chansz-python\project\charts\songs.json", "r") as f:
    data = json.load(f)
songs = data["songs"]

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
default_font = pygame.font.SysFont("Sans Serif", 50, True, True)
song_font = pygame.font.SysFont("Sans Serif", 40, False, False)
artist_font = pygame.font.SysFont("Sans Serif", 30, False, False)

BOX_WIDTH = 400
BOX_HEIGHT = 50
MENU_BOTTOM = HEIGHT
MENU_TOP = 60
visible_area = MENU_BOTTOM - MENU_TOP
scroll_offset = 0
selected = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if selected < len(songs) - 1:
                    selected = selected + 1
            elif event.key == pygame.K_UP:
                if selected > 0:
                    selected = selected - 1
        
    screen.fill(BLACK)

    #draw menu
    for i in range(len(songs)):
        pygame.draw.rect(screen, DARK_BLUE, (0, MENU_TOP + i * BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))
        song_text = song_font.render(songs[i]["name"], True, WHITE)
        artist_text = artist_font.render("By: " + songs[i]["artist"], True, WHITE)
        screen.blit(song_text, (20, MENU_TOP + i * BOX_HEIGHT + 10))
        screen.blit(artist_text, (200, MENU_TOP + i * BOX_HEIGHT + 20))
        if i == selected:
            pygame.draw.rect(screen, CYAN, (0, MENU_TOP + i * BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT), 3)
    
    #header
    pygame.draw.rect(screen, RED, (0, 0, 1280, 50))
    pygame.draw.line(screen, WHITE, (0, 50), (1280, 50), 3)
    title_text = default_font.render("Song Selection", True, WHITE)
    screen.blit(title_text, (20, 10))

    
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()