import pygame
from config import SNAKE_COLOR

class Snake:
    def __init__(self):
        self.size = 20
        self.positions = [(100, 100)]
        self.direction = pygame.K_RIGHT
        self.growing = False

    def update(self):
        x, y = self.positions[0]
        if self.direction == pygame.K_RIGHT:
            x += self.size
        elif self.direction == pygame.K_LEFT:
            x -= self.size
        elif self.direction == pygame.K_UP:
            y -= self.size
        elif self.direction == pygame.K_DOWN:
            y += self.size

        new_head = (x, y)
        
        if self.growing:
            self.positions = [new_head] + self.positions
            self.growing = False
        else:
            self.positions = [new_head] + self.positions[:-1]

    def grow(self):
        self.growing = True

    def change_direction(self, direction):
        opposite_directions = {pygame.K_UP: pygame.K_DOWN, pygame.K_DOWN: pygame.K_UP,
                               pygame.K_LEFT: pygame.K_RIGHT, pygame.K_RIGHT: pygame.K_LEFT}
        if direction != opposite_directions.get(self.direction):
            self.direction = direction

    def check_collision(self, playable_rect):
        head = self.positions[0]
        return (
            not playable_rect.collidepoint(head) or head in self.positions[1:]
        )

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, SNAKE_COLOR, (*pos, self.size, self.size))
