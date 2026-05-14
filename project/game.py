import os
import pygame
import time
import json

from config import *
from timing import Timing
from notes import *
from input import *
from loadNotes import *
from health import *
from background import *
from leaderboard import *

def run_game(screen, clock):
    from menu_screen import selected
    global perfect, good, bad, miss
    with open(r"C:\Users\cszel\OneDrive\Documents\GitHub\cs-project\project\charts\songs.json", "r") as f:
        data = json.load(f)
    songs = data["songs"]
    
    selected_song = songs[selected]

    pygame.mixer.init()
    pygame.mixer.music.load(selected_song["file"])

    font = pygame.font.SysFont("Arial", 30)
    artist_font = pygame.font.SysFont("Arial", 20)

    combo = 0
    combo_multiplier = 1
    health_bar = Health(screen)

    # Countdown before starting the song
    countdown_font = pygame.font.SysFont("Arial", 100, True, False)
    dim_layer = pygame.Surface((WIDTH, HEIGHT))
    dim_layer.fill((0, 0, 0))
    dim_layer.set_alpha(150)
    countdown_start = time.time()
    while True:
        tick = time.time() - countdown_start
        if tick < 1:
            countdown_text = "Ready"
        elif tick < 2:
            countdown_text = "Set"
        elif tick < 3:
            countdown_text = "Go!"
        else:
            break
        screen.fill((20, 20, 20))

        # Draw lanes and hit line
        pygame.draw.line(screen, WHITE, (450, Y_HIT_LINE), (850, Y_HIT_LINE), 3)
        pygame.draw.line(screen, WHITE, (450, 0), (450, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (550, 0), (550, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (650, 0), (650, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (750, 0), (750, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (850, 0), (850, HEIGHT), 3)
        health_bar.draw_hp_bar()

        screen.blit(dim_layer, (0, 0))
        text_surface = countdown_font.render(countdown_text, False, WHITE)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2 - text_surface.get_height() // 2))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.mixer.music.play()

    font = pygame.font.SysFont("Arial", 30)
    artist_font = pygame.font.SysFont("Arial", 20)

    hit_text = None
    text_timer = 0
    global score
    score = 0

    drum1 = Drum1(900, 426)
    drum2 = Drum2(900, 426)
    drum1_sprite = pygame.sprite.Group()
    drum1_sprite.add(drum1)
    drum2_sprite = pygame.sprite.Group()
    drum2_sprite.add(drum2)

    # Variables for swapping animations
    show_second_animation = False
    ANIMATION_DURATION = 150
    second_animation_timer = 0

    start_time = time.time()

    map_path = os.path.join(os.path.dirname(__file__), "charts", "autochart.json")
    notes = load_notes(map_path)
    
    global perfect
    global good
    global bad
    global miss
    global highest_combo
    perfect = 0
    good = 0
    bad = 0
    miss = 0
    highest_combo = 0
    
    global is_paused
    is_paused = False
    running = True
    while running:
        current_time = time.time() - start_time
        screen.fill((20, 20, 20))
        health_bar.draw_hp_bar()

        # Lines for lanes and hit detection line
        pygame.draw.line(screen, WHITE, (450, Y_HIT_LINE), (850, Y_HIT_LINE), 3)
        pygame.draw.line(screen, WHITE, (450, 0), (450, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (550, 0), (550, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (650, 0), (650, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (750, 0), (750, HEIGHT), 3)
        pygame.draw.line(screen, WHITE, (850, 0), (850, HEIGHT), 3)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_paused = not is_paused
                    if is_paused:
                        pause_result = paused(screen)
                        is_paused = False
                        if pause_result in ("Menu", "Game", "Quit"):
                            return pause_result
                if event.unicode in KEYS:
                    lane = KEYS.index(event.unicode)
                    # Show the second drum frame
                    show_second_animation = True
                    second_animation_timer = pygame.time.get_ticks()

                    if lane == 0:
                        pygame.draw.rect(screen, RED, (450, 610, 100, 110))
                    elif lane == 1:
                        pygame.draw.rect(screen, YELLOW, (550, 610, 100, 110))
                    elif lane == 2:
                        pygame.draw.rect(screen, GREEN, (650, 610, 100, 110))
                    elif lane == 3:
                        pygame.draw.rect(screen, BLUE, (750, 610, 100, 110))
                    for note in notes:
                        if note.lane == lane and note.hittable() and not note.hit:
                            result = isHit(note)
                            if result:
                                print(result)
                                if result == "Perfect!":
                                    combo = combo + 1
                                    if combo >= 10:
                                        multiplier = 1 + min(combo // 10, 10) / 10
                                        score = score + 100 * multiplier
                                        combo_multiplier = multiplier
                                    score = score + 100
                                    perfect = perfect + 1
                                    if combo > highest_combo:
                                        highest_combo = combo
                                elif result == "Good!":
                                    combo = combo + 1
                                    if combo >= 10:
                                        multiplier = 1 + min(combo // 10, 10) / 10
                                        score = score + 50 * multiplier
                                        combo_multiplier = multiplier
                                    score = score + 50
                                    good = good + 1
                                    if combo > highest_combo:
                                        highest_combo = combo
                                elif result == "Bad":
                                    multiplier = 1
                                    combo_multiplier = multiplier
                                    score = score + 10
                                    bad = bad + 1
                                    combo = 0
                                hit_text = result
                                text_timer = pygame.time.get_ticks()
                                note.hit = True
                                break

        for note in notes:
            if not note.hit:
                note.update(current_time)
                note.draw(screen, X_LANE[note.lane])

            if note.y > Y_HIT_LINE and not note.hit and not note.missed:
                note.missed = True
                miss = miss + 1
                combo = 0
                health_bar.deduct_hp()
                hit_text = "Miss"
                text_timer = pygame.time.get_ticks()
                
        if health_bar.get_hp() <= 0:
            return "GameOver"
            
        if hit_text:
            if pygame.time.get_ticks() - text_timer < 1000:
                text_surface = font.render(hit_text, False, WHITE)
                screen.blit(text_surface, (0, 0))
            else:
                hit_text = None

        song_text = selected_song["name"]
        artist_text = "By: " + selected_song["artist"]
        song_text_surface = font.render(song_text, False, WHITE)
        artist_text_surface = artist_font.render(artist_text, False, WHITE)
        screen.blit(song_text_surface, (0, 47))
        screen.blit(artist_text_surface, (0, 76))

        score_text = str(score)
        score_text_surface = font.render(score_text, False, WHITE)
        screen.blit(score_text_surface, (0, 189))

        combo_text = str(combo)
        multiplier_text = str(combo_multiplier)
        combo_text_surface = font.render("Combo: " + combo_text + " " + "(" + multiplier_text + "x" + ")", False, YELLOW)
        screen.blit(combo_text_surface, (0, 300))

        keybind_1 = KEYS[0]
        keybind1_text_surface = font.render(keybind_1, False, WHITE)
        screen.blit(keybind1_text_surface, (500, 610))
        keybind_2 = KEYS[1]
        keybind2_text_surface = font.render(keybind_2, False, WHITE)
        screen.blit(keybind2_text_surface, (600, 610))
        keybind_3 = KEYS[2]
        keybind3_text_surface = font.render(keybind_3, False, WHITE)
        screen.blit(keybind3_text_surface, (700, 610))
        keybind_4 = KEYS[3]
        keybind4_text_surface = font.render(keybind_4, False, WHITE)
        screen.blit(keybind4_text_surface, (800, 610))

        # Draw the correct animation
        if show_second_animation and pygame.time.get_ticks() - second_animation_timer < ANIMATION_DURATION:
            drum2_sprite.draw(screen)
        else:
            show_second_animation = False
            drum1_sprite.draw(screen)

        if not pygame.mixer.music.get_busy():
            running = False
            return "End"

        pygame.display.flip()
        clock.tick(FPS)

    return "Quit"
