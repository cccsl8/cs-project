import json
import pygame
from config import *
from generateNotes import generate_chart
from mutagen.mp3 import MP3

with open(r"C:\Users\cszel\OneDrive\Documents\GitHub\chansz-python\project\charts\songs.json", "r") as f:
    data = json.load(f)
songs = data["songs"]

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

default_font = pygame.font.SysFont("Arial", 20, False, False)
loading_font = pygame.font.SysFont("microsoftsansserif", 50, True, False)

pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()

def run_loading_screen(screen, clock):
    from menu_screen import selected
    
    song = MP3(songs[selected]["file"])

    chart = generate_chart(
    bpm = int(songs[selected]["bpm"]),
    song_length_seconds = int(song.info.length),
    lanes = 4,
    note_density = 0.5
    )

    with open("project/charts/autochart.json", "w") as f:
        json.dump(chart, f, indent = 4)
    print("Chart saved to charts/autochart.json")

    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return "Game"
                elif event.key == pygame.K_ESCAPE:
                    return "Menu"
            
            loading_text = loading_font.render("Loading...", False, WHITE)
            screen.blit(loading_text, (550, 331))

            enter_text = default_font.render("Press Enter to start.", False, WHITE)
            screen.blit(enter_text, (550, 426))

            escape_text = default_font.render("Press ESC to go back.", False, WHITE)
            screen.blit(escape_text, (550, 474))
            
            pygame.display.flip()
            clock.tick(FPS)

    return "Quit"
