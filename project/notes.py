import pygame
from config import NOTE_SPEED, Y_HIT_LINE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Note:
    def __init__(self, lane, spawn_time):
        self.lane = lane
        self.spawn_time = spawn_time
        self.y = -50
        self.hit = False
        self.missed = False
        self.spawned = False
    
    def update(self, current_time):
        if current_time < self.spawn_time:
            return
        if not self.spawned:
            self.spawned = True
        time_spawned = current_time - self.spawn_time
        self.y = time_spawned * NOTE_SPEED
    
    def draw(self, screen, x):
        pygame.draw.rect(screen, WHITE, (x - 25, self.y, 50, 20))
    
    def hittable(self):
        return abs(self.y - Y_HIT_LINE) < 60