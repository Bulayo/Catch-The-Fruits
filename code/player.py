from typing import Any
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, group: pygame.sprite.Group, pos: tuple[int], image: pygame.surface.Surface):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_frect(center = pos)
        self.direction = pygame.Vector2()
        self.speed = 300

    def update(self, dt):
        self.input()
        self.move(dt)

    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = (keys[pygame.K_RIGHT] or keys[pygame.K_d]) - (keys[pygame.K_LEFT] or keys[pygame.K_a])

    def move(self, dt):
        self.rect.x += self.direction.x * self.speed * dt