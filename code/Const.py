# =========================
# JANELA
# =========================

WIDTH = 1280
HEIGHT = 720
FPS = 60
TITLE = "Eternal Jump"

# =========================
# CORES
# =========================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (30, 50, 30)
BUTTON_HOVER_COLOR = (50, 80, 50)

# =========================
# MENU
# =========================

MENU_IMAGE = "assets/BackgroundMenu.png"
MENU_MUSIC = "assets/Music_Menu.wav"
CLICK_SOUND = "assets/GameStart.ogg"

# =========================
# JOGO
# =========================
# Camadas do fundo com efeito de paralaxe
LAYERS = [
    ("assets/sky.png", 0.1),
    ("assets/jungle_bg.png", 0.2),
    ("assets/trees_bushes.png", 0.5),
    ("assets/lianas.png", 0.6),
    ("assets/grasses.png", 1.0),
    ("assets/fireflys.png", 0.7),
    ("assets/grass_road.png", 1.0),
    ("assets/trees_face.png", 1.0),
]

GAME_MUSIC = "assets/Music_Game.wav"
JUMP_SOUND = "assets/Jump.wav"
GAME_OVER_SOUND = "assets/GameOver.wav"

PLAYER_IMG = "assets/Player.png"
OBSTACLE_IMG = "assets/Obstacle.png"

# =========================
# POSIÇÕES
# =========================

GROUND_Y = HEIGHT - 120

# =========================
# FÍSICA
# =========================

GRAVITY = 0.8
JUMP_VELOCITY = -24

# =========================
# DIFICULDADE
# =========================

DIFFICULTIES = {
    "facil": {
        "initial_speed": 7,
        "speed_increment": 1.0,
        "obstacle_interval": 1300
    },
    "dificil": {
        "initial_speed": 9,
        "speed_increment": 1.1,
        "obstacle_interval": 1200
    },
    "impossivel": {
        "initial_speed": 12,
        "speed_increment": 1.3,
        "obstacle_interval": 900
    }
}