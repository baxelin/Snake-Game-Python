import pygame
from config import FONT, WHITE, BACKGROUND_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Options:
    def __init__(self):
        self.speeds = [0.5, 1, 2, 4]
        self.speed_index = 1  # Começa com a velocidade normal (1x)

    def increase_speed(self):
        self.speed_index = min(self.speed_index + 1, len(self.speeds) - 1)

    def decrease_speed(self):
        self.speed_index = max(self.speed_index - 1, 0)

    def get_speed(self):
        return self.speeds[self.speed_index]

    def display(self, screen):
        # Exibe as opções de velocidade na tela
        screen.fill(BACKGROUND_COLOR)
        title_text = FONT.render("Opções de Configuração", True, WHITE)
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 100))

        # Exibe a velocidade atual configurável
        speed_text = FONT.render(f"Velocidade: {self.speeds[self.speed_index]}x", True, WHITE)
        screen.blit(speed_text, (SCREEN_WIDTH // 2 - speed_text.get_width() // 2, SCREEN_HEIGHT // 2))
        
        # Instruções para mudar a velocidade
        instructions_text = FONT.render("Use ←/→ para ajustar", True, WHITE)
        screen.blit(instructions_text, (SCREEN_WIDTH // 2 - instructions_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))

        pygame.display.flip()
