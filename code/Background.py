import pygame

class Background:
    """
    Fundo com rolagem infinita e efeito de paralaxe.
    Camadas que devem se mover juntas podem ter o mesmo speed_factor.
    """

    def __init__(self, layers, width, height):
        """
        layers: lista de tuplas (caminho_imagem, speed_factor)
        width, height: tamanho da tela
        """
        self.width = width
        self.height = height
        self.layers = []

        for path, speed_factor in layers:
            try:
                img = pygame.image.load(path).convert_alpha()
            except FileNotFoundError:
                print(f"[Warning] Arquivo não encontrado: {path}")
                continue
            img = pygame.transform.scale(img, (width, height))
            self.layers.append({
                "image": img,
                "x": 0.0,
                "speed_factor": speed_factor
            })

    def update(self, base_speed):
        """
        Atualiza posição de cada camada.
        base_speed: velocidade base do jogo
        """
        for layer in self.layers:
            layer["x"] -= base_speed * layer["speed_factor"]
            if layer["x"] <= -self.width:
                layer["x"] += self.width  # loop infinito suave

    def draw(self, screen):
        """
        Desenha todas as camadas na tela, lado a lado para efeito infinito
        """
        for layer in self.layers:
            x = int(layer["x"])
            screen.blit(layer["image"], (x, 0))
            screen.blit(layer["image"], (x + self.width, 0))