import pygame
import random
from code.menu import Menu
from code.const import *
from code.player import Player
from code.obstacle import Obstacle

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # Menu
        self.menu = Menu(self.screen)
        self.state = "menu"
        self.best_score = 0

        # Fundo
        self.bg = pygame.image.load(GAME_BG).convert()
        self.bg = pygame.transform.scale(self.bg, (WIDTH, HEIGHT))
        self.bg_x = 0

        # Player
        self.player = Player(150, GROUND_Y)
        self.obstacles = []

        # Spawn de obstáculos
        self.last_obstacle_time = pygame.time.get_ticks()
        self.next_obstacle_delay = random.randint(1200, 2000)

        # Score por tempo
        self.start_time = 0
        self.score = 0

        # Velocidade
        self.base_speed = INITIAL_SPEED
        self.speed = INITIAL_SPEED

        # Sons
        self.menu_music = pygame.mixer.Sound(MENU_MUSIC)
        self.menu_music.set_volume(0.5)
        self.game_music = pygame.mixer.Sound(GAME_MUSIC)
        self.game_music.set_volume(0.5)
        self.game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
        self.game_over_sound.set_volume(0.5)
        self.jump_sound = pygame.mixer.Sound(JUMP_SOUND)
        self.jump_sound.set_volume(0.5)

        # Começa com música do menu
        self.menu_music.play(-1)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pygame.quit()

    def start_game(self):
        self.state = "play"

        # Para todas as músicas
        self.menu_music.stop()
        self.game_music.stop()
        self.game_over_sound.stop()

        self.obstacles.clear()
        self.player.reset()

        self.start_time = pygame.time.get_ticks()
        self.score = 0
        self.speed = self.base_speed

        self.last_obstacle_time = pygame.time.get_ticks()
        self.next_obstacle_delay = random.randint(1200, 2000)

        # Toca música do jogo
        self.game_music.play(-1)

    def game_over(self):
        self.game_music.stop()
        self.game_over_sound.play()

        if self.score > self.best_score:
            self.best_score = self.score

        self.state = "menu"

        # Volta música do menu
        self.menu_music.stop()
        self.menu_music.play(-1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "menu":
                action = self.menu.check_click(event)
                if action == "play":
                    self.start_game()

            elif self.state == "play":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
                        self.jump_sound.play()

    def update(self):
        if self.state != "play":
            return

        current_time = pygame.time.get_ticks()

        # Score por tempo
        self.score = (current_time - self.start_time) // 100

        # Velocidade aumenta com o tempo
        self.speed = self.base_speed + (self.score * 0.02)

        # Fundo em movimento
        self.bg_x -= self.speed
        if self.bg_x <= -WIDTH:
            self.bg_x = 0

        self.player.update()

        # Spawn obstáculos inteligente
        if current_time - self.last_obstacle_time > self.next_obstacle_delay:
            if not self.obstacles or self.obstacles[-1].rect.x < WIDTH - 450:
                self.obstacles.append(Obstacle(WIDTH, GROUND_Y))
                self.last_obstacle_time = current_time
                self.next_obstacle_delay = random.randint(1200, 2000)

        # Atualiza obstáculos e checa colisão
        for obstacle in self.obstacles[:]:
            obstacle.update(self.speed)

            if obstacle.rect.right < 0:
                self.obstacles.remove(obstacle)

            if self.player.rect.colliderect(obstacle.hitbox):
                self.game_over()

    def draw(self):
        if self.state == "menu":
            self.menu.best_score = self.best_score
            self.menu.draw()
            return

        # Fundo infinito
        self.screen.blit(self.bg, (self.bg_x, 0))
        self.screen.blit(self.bg, (self.bg_x + WIDTH, 0))

        # Player
        self.player.draw(self.screen)

        # Obstáculos
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # Score
        font = pygame.font.SysFont("arial", 30)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (20, 20))

        pygame.display.update()