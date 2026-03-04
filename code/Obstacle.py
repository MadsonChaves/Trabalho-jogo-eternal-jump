import random

import pygame

from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, x, y):
        # Carrega imagens
        obstacle_images = [
            pygame.image.load("assets/obstacle1.png").convert_alpha(),
            pygame.image.load("assets/obstacle2.png").convert_alpha(),
            pygame.image.load("assets/obstacle3.png").convert_alpha(),
        ]

        original_image = random.choice(obstacle_images)
        image = pygame.transform.scale(original_image, (80, 110))

        # Inicializa Entity
        super().__init__(image, (x, y))

        # Hitbox menor que a imagem
        self.hitbox = pygame.Rect(
            self.rect.x + 20,
            self.rect.y + 30,
            self.rect.width - 40,
            self.rect.height - 40,
        )

        # Posição horizontal com float para movimento suave
        self.pos_x = float(self.rect.x)

    def update(self, speed):
        # Move para esquerda usando float
        self.pos_x -= speed
        self.rect.x = int(self.pos_x)
        self.hitbox.x = self.rect.x