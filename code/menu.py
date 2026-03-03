import pygame
from code.const import *

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.best_score = 0

        # Fundo
        self.bg = pygame.image.load(MENU_IMAGE).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))

        # Fonte
        self.font = pygame.font.SysFont("arial", 50)

        # Botão central
        self.button_rect = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 60)

        # Som de clique
        self.click_sound = pygame.mixer.Sound(CLICK_SOUND)
        self.click_sound.set_volume(0.5)

    def draw(self):
        self.screen.blit(self.bg, (0, 0))

        # Título
        title_text = self.font.render(TITLE, True, WHITE)
        self.screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 150))

        # Botão
        mouse_pos = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if self.button_rect.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, self.button_rect, border_radius=10)

        play_text = self.font.render("Jogar", True, WHITE)
        self.screen.blit(
            play_text,
            (
                self.button_rect.centerx - play_text.get_width()//2,
                self.button_rect.centery - play_text.get_height()//2
            )
        )

        # Melhor score
        best_text = self.font.render(f"Melhor tempo: {self.best_score}", True, WHITE)
        self.screen.blit(best_text, (WIDTH//2 - best_text.get_width()//2, 250))

        pygame.display.update()

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_rect.collidepoint(event.pos):
                self.click_sound.play()
                return "play"
        return None