import pygame
from config import *
import json
import os
from album_covers import *

with open(r"C:\Users\cszel\OneDrive\Documents\GitHub\cs-project\project\charts\songs.json", "r") as f:
    data = json.load(f)
songs = data["songs"]

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
default_font = pygame.font.SysFont("microsoftsansserif", 30, True, True)
song_font = pygame.font.SysFont("microsoftsansserif", 20, False, False)
artist_font = pygame.font.SysFont("microsoftsansserif", 20, False, False)
song_info_font = pygame.font.SysFont("Arial", 20, False, False)
difficulty_font = pygame.font.SysFont("Arial", 20, False, True)

BOX_WIDTH = 600
BOX_HEIGHT = 50
MENU_BOTTOM = HEIGHT
MENU_TOP = 60
visible_area = MENU_BOTTOM - MENU_TOP
scroll_offset = 0
selected = 0

def run_menu_screen(screen, clock):
    global selected
    
    # Making sure selected is within the range of the song list
    if selected >= len(songs):
        selected = len(songs) - 1
    if selected < 0:
        selected = 0
    
    dim_layer = pygame.Surface((WIDTH, HEIGHT))
    dim_layer.fill((0, 0, 0))
    dim_layer.set_alpha(128)

    running = True
    while running:
        album_cover = AlbumCover(800, 100, selected)
        album_group = pygame.sprite.Group()
        album_group.add(album_cover)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if selected < len(songs) - 1:
                        selected = selected + 1
                        print("Seletcted: " + songs[selected]["name"])
                elif event.key == pygame.K_UP:
                    if selected > 0:
                        selected = selected - 1
                        print("Seletcted: " + songs[selected]["name"])
                elif event.key == pygame.K_RETURN:
                    running = False
                    return "Loading"
                
        screen.fill(BLACK)

        #background
        bg = pygame.image.load(songs[selected]["background"])
        bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
        screen.blit(bg, bg.get_rect())
        screen.blit(dim_layer, (0, 0))

        #draw menu
        for i in range(len(songs)):
            pygame.draw.rect(screen, DARK_BLUE, (0, MENU_TOP + i * BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT))
            song_text = song_font.render(songs[i]["name"], True, WHITE)
            screen.blit(song_text, (20, MENU_TOP + i * BOX_HEIGHT + 10))
            if i == selected:
                pygame.draw.rect(screen, CYAN, (0, MENU_TOP + i * BOX_HEIGHT, BOX_WIDTH, BOX_HEIGHT), 3)

        #header
        pygame.draw.rect(screen, BLUE, (0, 0, 1280, 50))
        pygame.draw.line(screen, WHITE, (0, 50), (1280, 50), 3)
        title_text = default_font.render("Song Selection", True, WHITE)
        screen.blit(title_text, (20, 10))
        
        #display song details
        album_group.draw(screen)
        pygame.draw.rect(screen, WHITE, album_cover.rect, 2)
        bpm_text = song_info_font.render("BPM: "+ str(songs[selected]["bpm"]), True, WHITE)
        screen.blit(bpm_text, (900, 426))
        artist_text = artist_font.render("By: " + songs[selected]["artist"], True, WHITE)
        screen.blit(artist_text, (900, 401))
        difficulty_text = difficulty_font.render("Difficulty: " + str(songs[selected]["difficulty"]), True, WHITE)
        screen.blit(difficulty_text, (900, 474))

        pygame.display.flip()
        clock.tick(FPS)
    
    return "Quit"