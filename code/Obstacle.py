import pygame
import random
from code.Entity import Entity


class Obstacle(Entity):
    """
    Classe que representa os obstáculos do jogo.
    """

    def __init__(self, x, y):
        # Carrega imagens possíveis
        obstacle_images = [
            pygame.image.load("assets/obstacle1.png").convert_alpha(),
            pygame.image.load("assets/obstacle2.png").convert_alpha(),
            pygame.image.load("assets/obstacle3.png").convert_alpha(),
        ]

        # Escolhe uma imagem aleatória
        original_image = random.choice(obstacle_images)

        # Redimensiona
        image = pygame.transform.scale(original_image, (80, 110))

        # Inicializa Entity
        super().__init__(image, (x, y))

        # Hitbox menor que a imagem (colisão mais justa)
        self.hitbox = pygame.Rect(
            self.rect.x + 20,
            self.rect.y + 30,
            self.rect.width - 40,
            self.rect.height - 40,
        )

    def update(self, speed):
        # Move para esquerda
        self.rect.x -= speed
        self.hitbox.x -= speed