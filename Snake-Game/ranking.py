import pygame
from config import FONT, WHITE, BACKGROUND_COLOR, SCREEN_WIDTH

class Ranking:
    def __init__(self):
        self.scores = []

    def add_score(self, score, time):
        self.scores.append((score, time))
        self.scores = sorted(self.scores, key=lambda x: x[0], reverse=True)[:10]

    def display(self, screen):
        screen.fill(BACKGROUND_COLOR)
        for index, (score, time) in enumerate(self.scores):
            text = FONT.render(f"{index + 1}. Pontuação: {score} - Tempo: {time:.1f}s", True, WHITE)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150 + index * 30))
        pygame.display.flip()
        pygame.time.delay(3000)  # Exibe o ranking por 3 segundos
