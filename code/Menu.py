import pygame
from code.Const import *


class Menu:
    """
    Tela inicial do jogo com seleção de dificuldade.
    Exibe título, melhores tempos, botões de dificuldade e comandos de controle.
    """

    def __init__(self, screen):
        self.screen = screen
        self.best_score = 0

        # Fundo
        self.bg = pygame.image.load(MENU_IMAGE).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

        # Fonte
        self.font = pygame.font.SysFont("arial", 50)
        self.small_font = pygame.font.SysFont("arial", 35)

        # Botões de dificuldade
        self.buttons = {
            "facil": pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 - 20, 240, 55),
            "dificil": pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 50, 240, 55),
            "impossivel": pygame.Rect(WIDTH // 2 - 120, HEIGHT // 2 + 120, 240, 55),
        }

        # Som de clique
        self.click_sound = pygame.mixer.Sound(CLICK_SOUND)
        self.click_sound.set_volume(0.5)

    def draw(self):
        # Fundo
        self.screen.blit(self.bg, (0, 0))

        # Título
        title_text = self.font.render(TITLE, True, WHITE)
        self.screen.blit(
            title_text,
            (WIDTH // 2 - title_text.get_width() // 2, 130)
        )

        mouse_pos = pygame.mouse.get_pos()

        # Desenha botões
        for name, rect in self.buttons.items():
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR

            pygame.draw.rect(
                self.screen,
                color,
                rect,
                border_radius=10
            )

            text = self.small_font.render(name.capitalize(), True, WHITE)
            self.screen.blit(
                text,
                (
                    rect.centerx - text.get_width() // 2,
                    rect.centery - text.get_height() // 2
                )
            )

        # Melhor score
        best_text = self.small_font.render(
            f"Melhor tempo: {self.best_score}",
            True,
            WHITE
        )
        self.screen.blit(
            best_text,
            (WIDTH // 2 - best_text.get_width() // 2, 250)
        )

        # Comandos de controle
        jump_text = self.small_font.render("Space - Saltar", True, WHITE)
        self.screen.blit(jump_text, (20, HEIGHT - 80))

        pygame.display.update()

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for name, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    self.click_sound.play()
                    return name  # retorna "facil", "dificil" ou "impossivel"

        return None