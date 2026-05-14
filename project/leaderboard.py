import json
import os
import pygame
from config import *
from datetime import datetime

screen = pygame.display.set_mode([WIDTH, HEIGHT])
default_font = pygame.font.SysFont("Arial", 30, False, False)
large_font = pygame.font.SysFont("Arial", 50, True, False)

SCORES_FILE = r"C:\Users\cszel\OneDrive\Documents\GitHub\cs-project\project\scores.json"

class Leaderboard:
    def __init__(self, filename = SCORES_FILE, max_entries = 10):
        self.filename = filename
        self.max_entries = max_entries
        self.scores = self.load()

    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []
    
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.scores, f, indent=2)
    
    def add_score(self, name, score):
        entry = {
            "name": name,
            "score": score,
            "date": datetime.now()
        }
        self.scores.append(entry)
        self.scores.sort(key=lambda x: x["score"], reverse=True)
        self.scores = self.scores[:self.max_entries]
        self.save()
    
    def is_high_score(self, score):
        if len(self.score) < self.max_entries:
            return True
        return score > self.scores[-1]["scores"]
    
def draw_leaderboard(leaderboard):
    screen.fill((20, 20, 40))
    title = large_font.render("Leaderboard", True, WHITE)
    screen.blit(title, (WIDTH // 2 - 50, 10))

    for i, entry in enumerate(leaderboard.scores):
        if i == 0:
            colour = YELLOW
        else:
            colour = WHITE
        text = f"{i+1}. {entry['name']:<15} {entry['score']:>6}   {entry['date']}"
        text_surface = default_font.render(text, True, colour)
        screen.blit(text_surface, (100, 130 + i * 40))
    
def draw_enter_name(score, player_name):
    screen.fill((20, 20, 40))
    new_high_score = large_font.render("New high score!", True, (YELLOW))
    screen.blit(new_high_score, (WIDTH // 2 - 100, 30))
    
    score_surface = default_font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_surface, (WIDTH // 2, 240))

    name_surf = default_font.render(f"Enter name: {player_name}", True, (100, 220, 255))
    screen.blit(name_surf, (WIDTH // 2, 310))
