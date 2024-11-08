import pygame
from config import (
    FONT, WHITE, BLACK, SNAKE_COLOR, APPLE_COLOR, BACKGROUND_COLOR,
    PLAYABLE_BG_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT,
    PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT, BORDER_WIDTH
)
from snake import Snake
from apple import Apple
from menu import Menu
from ranking import Ranking
from options import Options

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.apple = Apple()
        self.menu = Menu()
        self.ranking = Ranking()
        self.options = Options()
        self.score = 0
        self.running = True
        self.in_game = False
        self.start_time = None

        # Área jogável com borda
        self.playable_rect = pygame.Rect(
            (SCREEN_WIDTH - PLAYABLE_AREA_WIDTH) // 2,
            (SCREEN_HEIGHT - PLAYABLE_AREA_HEIGHT) // 2,
            PLAYABLE_AREA_WIDTH,
            PLAYABLE_AREA_HEIGHT
        )

    def reset(self):
        self.snake = Snake()
        self.apple.spawn(self.playable_rect)
        self.score = 0
        self.start_time = pygame.time.get_ticks()

    def countdown(self):
        for i in range(3, 0, -1):
            self.screen.fill(BACKGROUND_COLOR)
            count_text = FONT.render(str(i), True, WHITE)
            self.screen.blit(count_text, (SCREEN_WIDTH // 2 - count_text.get_width() // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            pygame.time.delay(1000)

    def run(self):
        while self.running:
            self.handle_events()
            if self.in_game:
                self.update()
                self.draw()
                self.clock.tick(15 * self.options.get_speed())  # Ajusta velocidade da cobra
            else:
                self.menu.display(self.screen)
            self.clock.tick(15)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.in_game:
                    self.handle_game_keys(event.key)
                else:
                    self.handle_menu_keys(event.key)

    def handle_game_keys(self, key):
        if key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            self.snake.change_direction(key)

    def handle_menu_keys(self, key):
        if key == pygame.K_DOWN:
            self.menu.navigate("DOWN")
        elif key == pygame.K_UP:
            self.menu.navigate("UP")
        elif key == pygame.K_RETURN:
            selected_option = self.menu.get_selected_option()
            if selected_option == "Jogar":
                self.reset()
                self.countdown()
                self.in_game = True
            elif selected_option == "Ranking":
                self.ranking.display(self.screen)
            elif selected_option == "Opções":
                self.show_options()

    def show_options(self):
        adjusting = True
        while adjusting:
            self.options.display(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    adjusting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.options.decrease_speed()
                    elif event.key == pygame.K_RIGHT:
                        self.options.increase_speed()
                    elif event.key == pygame.K_RETURN:
                        adjusting = False

    def update(self):
        self.snake.update()
        if self.snake.check_collision(self.playable_rect):
            self.in_game = False
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
            self.ranking.add_score(self.score, elapsed_time)

        if self.snake.positions[0] == self.apple.position:
            self.snake.grow()
            self.apple.spawn(self.playable_rect)
            self.score += 1

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        pygame.draw.rect(self.screen, BLACK, self.playable_rect, BORDER_WIDTH)
        pygame.draw.rect(self.screen, PLAYABLE_BG_COLOR, self.playable_rect)

        # Desenha cobra, maçã e pontuação
        self.snake.draw(self.screen)
        self.apple.draw(self.screen)
        score_text = FONT.render(f"Pontuação: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))

        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000
        timer_text = FONT.render(f"Tempo: {elapsed_time:.1f}s", True, WHITE)
        self.screen.blit(timer_text, (SCREEN_WIDTH - timer_text.get_width() - 20, 10))

        pygame.display.flip()
