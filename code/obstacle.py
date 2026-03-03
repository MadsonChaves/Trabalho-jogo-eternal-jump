import pygame
import random
from code.const import *

class Obstacle:
    def __init__(self, x, y):
        obstacle_images = [
            pygame.image.load("assets/obstacle1.png").convert_alpha(),
            pygame.image.load("assets/obstacle2.png").convert_alpha(),
            pygame.image.load("assets/obstacle3.png").convert_alpha()
        ]

        original_image = random.choice(obstacle_images)

        self.image = pygame.transform.scale(original_image, (80, 110))

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        #  HITBOX PERSONALIZADA (menor que a imagem)
        self.hitbox = pygame.Rect(
            self.rect.x + 20,
            self.rect.y + 30,
            self.rect.width - 40,
            self.rect.height - 40
        )

    def update(self, speed):
        self.rect.x -= speed
        self.hitbox.x -= speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)