import pygame
from config import FONT, WHITE, BACKGROUND_COLOR, SCREEN_WIDTH

class Menu:
    def __init__(self):
        self.options = ["Jogar", "Ranking", "Opções"]
        self.selected_option = 0

    def display(self, screen):
        screen.fill(BACKGROUND_COLOR)
        for index, option in enumerate(self.options):
            color = WHITE if index == self.selected_option else (96, 108, 56)  # Destaque da opção selecionada
            text = FONT.render(option, True, color)
            screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 150 + index * 50))
        pygame.display.flip()

    def navigate(self, direction):
        if direction == "UP":
            self.selected_option = (self.selected_option - 1) % len(self.options)
        elif direction == "DOWN":
            self.selected_option = (self.selected_option + 1) % len(self.options)

    def get_selected_option(self):
        return self.options[self.selected_option]
