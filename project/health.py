import pygame
from input import *
from config import WIDTH, HEIGHT

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class Health:
    def __init__(self, screen):
        global font
        self.screen = screen
        self.hp = 100
        self.hp_bar_width = 100
        self.hp_bar_colour = GREEN
        font = pygame.font.SysFont("Arial", 25)
    
    def draw_hp_bar(self):
        pygame.draw.rect(self.screen, self.hp_bar_colour, (10, 474, self.hp_bar_width, 20))
        hp_text = "HP: " + str(self.hp)
        hp_text_surface = font.render(hp_text, False, WHITE)
        self.screen.blit(hp_text_surface, (10, 440))
    
    def deduct_hp(self):
        if self.hp > 0:
            self.hp = self.hp - 10
            self.hp_bar_width = self.hp_bar_width - 10
        if self.hp <= 50:
            self.hp_bar_colour = RED
    
    def get_hp(self):
        return self.hp
        