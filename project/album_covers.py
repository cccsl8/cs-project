import pygame
from config import *

album_cover_list = [
    "whiplash cover.jpg",
    "BR_cover.jpg",
    "nirvana album cover.jpg"
]

class AlbumCover(pygame.sprite.Sprite):
    def __init__(self, x, y, i):
        super().__init__()
        self.image = pygame.image.load(album_cover_list[i]).convert()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y