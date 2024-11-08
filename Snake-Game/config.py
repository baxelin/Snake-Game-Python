import pygame

# Configurações globais
pygame.init()

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SNAKE_COLOR = (96, 108, 56)        # #606c38
APPLE_COLOR = (214, 40, 40)        # #d62828
BACKGROUND_COLOR = (221, 161, 94)  # #dda15e
PLAYABLE_BG_COLOR = (254, 250, 224) # #fefae0
BORDER_COLOR = BLACK               # Cor da borda ao redor da área jogável

# Dimensões da tela e da área jogável
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYABLE_AREA_WIDTH = 600
PLAYABLE_AREA_HEIGHT = 400
BORDER_WIDTH = 10  # Largura da borda ao redor da área jogável

INITIAL_SPEED = 10
FONT = pygame.font.Font(None, 36)

GREEN = (0, 255, 0)  # Verde padrão, caso ainda seja usado em outros lugares
