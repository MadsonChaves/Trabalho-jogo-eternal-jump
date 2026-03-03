import pygame
from code.const import *

class Player:
    def __init__(self, x, y):
        self.run_sheet = pygame.image.load("assets/run.png").convert_alpha()
        self.jump_sheet = pygame.image.load("assets/jump.png").convert_alpha()

        self.frame_width = 128
        self.frame_height = 128

        self.run_frames = self.load_frames(self.run_sheet, 9)
        self.jump_frames = self.load_frames(self.jump_sheet, 11)

        self.scale_size = 210
        self.run_frames = [pygame.transform.scale(f, (self.scale_size, self.scale_size)) for f in self.run_frames]
        self.jump_frames = [pygame.transform.scale(f, (self.scale_size, self.scale_size)) for f in self.jump_frames]

        self.current_frames = self.run_frames
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = self.current_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)

        self.vel_y = 0

        # Som de pulo
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.jump_sound.set_volume(0.5)

    def load_frames(self, sheet, frames):
        frame_list = []
        for i in range(frames):
            frame = sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height))
            frame_list.append(frame)
        return frame_list

    def jump(self):
        if self.rect.bottom >= GROUND_Y:
            self.vel_y = JUMP_VELOCITY
            self.jump_sound.play()  # Toca som apenas se o pulo acontece

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.current_frames = self.run_frames
        else:
            self.current_frames = self.jump_frames

        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.current_frames):
            self.frame_index = 0

        self.image = self.current_frames[int(self.frame_index)]

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):
        self.rect.midbottom = (150, GROUND_Y)
        self.vel_y = 0