import pygame
from code.Const import *
from code.Entity import Entity


class Player(Entity):
    """
    Classe do jogador.
    Controla animação, física e pulo.
    """

    def __init__(self, x, y):
        # Carrega sprites
        self.run_sheet = pygame.image.load("assets/run.png").convert_alpha()
        self.jump_sheet = pygame.image.load("assets/jump.png").convert_alpha()

        self.frame_width = 128
        self.frame_height = 128

        # Separa os frames
        self.run_frames = self.load_frames(self.run_sheet, 9)
        self.jump_frames = self.load_frames(self.jump_sheet, 11)

        # Redimensiona os sprites
        self.scale_size = 210
        self.run_frames = [
            pygame.transform.scale(f, (self.scale_size, self.scale_size))
            for f in self.run_frames
        ]
        self.jump_frames = [
            pygame.transform.scale(f, (self.scale_size, self.scale_size))
            for f in self.jump_frames
        ]

        # Define animação inicial
        self.current_frames = self.run_frames
        self.frame_index = 0
        self.animation_speed = 0.15

        # Inicializa Entity com primeira imagem
        super().__init__(self.current_frames[0], (x, y))

        # Física
        self.vel_y = 0

        # Som de pulo
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.jump_sound.set_volume(0.5)

    def load_frames(self, sheet, frames):
        # Extrai os frames da sprite sheet
        frame_list = []
        for i in range(frames):
            frame = sheet.subsurface(
                (i * self.frame_width, 0, self.frame_width, self.frame_height)
            )
            frame_list.append(frame)
        return frame_list

    def jump(self):
        # Só pula se estiver no chão
        if self.rect.bottom >= GROUND_Y:
            self.vel_y = JUMP_VELOCITY
            self.jump_sound.play()

    def update(self):
        # Aplica gravidade
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Verifica se tocou o chão
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.current_frames = self.run_frames
        else:
            self.current_frames = self.jump_frames

        # Atualiza animação
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.current_frames):
            self.frame_index = 0

        self.image = self.current_frames[int(self.frame_index)]

    def reset(self):
        # Reinicia posição e velocidade
        self.rect.midbottom = (150, GROUND_Y)
        self.vel_y = 0