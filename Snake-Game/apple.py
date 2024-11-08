import pygame
import random
from config import APPLE_COLOR

class Apple:
    def __init__(self):
        self.position = (0, 0)

    def spawn(self, playable_rect):
        x = random.randint(playable_rect.left // 20, (playable_rect.right - 20) // 20) * 20
        y = random.randint(playable_rect.top // 20, (playable_rect.bottom - 20) // 20) * 20
        self.position = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, APPLE_COLOR, (*self.position, 20, 20))
