import pygame

class Entity:
    """
    Classe base para objetos do jogo.
    """

    def __init__(self, image, position):
        # Imagem (sprite) da entidade
        self.image = image

        # Retângulo usado para posição e colisão
        self.rect = self.image.get_rect()
        self.rect.midbottom = position

    def update(self, *args):
        # Método que pode ser sobrescrito pelas subclasses
        pass

    def draw(self, screen):
        # Desenha a entidade na tela
        screen.blit(self.image, self.rect)