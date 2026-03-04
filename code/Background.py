import pygame


class Background:
    """
    Controla o fundo com efeito de rolagem infinita.
    """

    def __init__(self, image_path, width, height):
        # Carrega e redimensiona a imagem
        self.image = pygame.image.load(image_path).convert()
        self.image = pygame.transform.scale(self.image, (width, height))

        self.width = width
        self.x = 0  # Posição horizontal do fundo

    def update(self, speed):
        # Move o fundo para a esquerda
        self.x -= speed

        # Reinicia posição para criar efeito infinito
        if self.x <= -self.width:
            self.x = 0

    def draw(self, screen):
        # Desenha duas imagens lado a lado para criar loop infinito
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + self.width, 0))