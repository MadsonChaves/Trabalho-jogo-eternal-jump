import pygame
import random
from code.Menu import Menu
from code.Const import *
from code.Const import LAYERS  # import correto
from code.Player import Player
from code.Obstacle import Obstacle
from code.Background import Background


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # Fonte do score
        self.font = pygame.font.SysFont("arial", 30)

        # Estado
        self.state = "menu"
        self.best_score = 0
        self.difficulty = "dificil"

        # Menu
        self.menu = Menu(self.screen)

        # Background com paralaxe
        self.background = Background(LAYERS, WIDTH, HEIGHT)

        # Player
        self.player = Player(150, GROUND_Y)
        self.obstacles = []

        # Spawn
        self.last_obstacle_time = pygame.time.get_ticks()
        self.next_obstacle_delay = 1500

        # Score
        self.start_time = 0
        self.score = 0

        # Velocidade inicial
        self.speed = DIFFICULTIES[self.difficulty]["initial_speed"]

        # Sons
        self.menu_music = pygame.mixer.Sound(MENU_MUSIC)
        self.menu_music.set_volume(0.5)

        self.game_music = pygame.mixer.Sound(GAME_MUSIC)
        self.game_music.set_volume(0.5)

        self.game_over_sound = pygame.mixer.Sound(GAME_OVER_SOUND)
        self.game_over_sound.set_volume(0.5)

        # Música inicial
        self.menu_music.play(-1)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

        pygame.quit()

    def start_game(self, difficulty):
        self.difficulty = difficulty
        config = DIFFICULTIES[self.difficulty]

        self.state = "play"

        self.menu_music.stop()
        self.game_music.stop()
        self.game_over_sound.stop()

        self.obstacles.clear()
        self.player.reset()

        self.start_time = pygame.time.get_ticks()
        self.score = 0

        # Configuração baseada na dificuldade
        self.speed = config["initial_speed"]
        self.next_obstacle_delay = config["obstacle_interval"]
        self.last_obstacle_time = pygame.time.get_ticks()

        self.game_music.play(-1)

    def game_over(self):
        self.game_music.stop()
        self.game_over_sound.play()

        if self.score > self.best_score:
            self.best_score = self.score

        self.state = "menu"

        self.menu_music.stop()
        self.menu_music.play(-1)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if self.state == "menu":
                action = self.menu.check_click(event)
                if action:
                    self.start_game(action)

            elif self.state == "play":
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()

    def update(self):
        if self.state != "play":
            return

        current_time = pygame.time.get_ticks()
        config = DIFFICULTIES[self.difficulty]

        # Score
        self.score = (current_time - self.start_time) // 100

        # Velocidade aumenta com o tempo
        self.speed = config["initial_speed"] + (self.score * 0.02 * config["speed_increment"])

        # Atualiza fundo com paralaxe
        self.background.update(self.speed)

        # Atualiza player
        self.player.update()

        # Spawn obstáculos baseado na dificuldade
        if current_time - self.last_obstacle_time > self.next_obstacle_delay:
            if not self.obstacles or self.obstacles[-1].rect.x < WIDTH - 450:
                self.obstacles.append(Obstacle(WIDTH, GROUND_Y))
                self.last_obstacle_time = current_time
                self.next_obstacle_delay = config["obstacle_interval"]

        # Atualiza obstáculos
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

        # Fundo
        self.background.draw(self.screen)

        # Player
        self.player.draw(self.screen)

        # Obstáculos
        for obstacle in self.obstacles:
            obstacle.draw(self.screen)

        # Score
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        diff_text = self.font.render(f"Modo: {self.difficulty}", True, WHITE)
        self.screen.blit(score_text, (20, 20))
        self.screen.blit(diff_text, (20, 55))
        pygame.display.update()