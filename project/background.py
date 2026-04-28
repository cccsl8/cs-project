import pygame

BLACK = (0, 0, 0)

class Drum1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("drummer1.jpg").convert()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Drum2(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("drummer2.jpg").convert()
        self.image = pygame.transform.scale(self.image, (300, 300))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y