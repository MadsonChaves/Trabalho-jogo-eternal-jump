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

GAME_BG = "assets/BackgroundGame.png"
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
JUMP_VELOCITY = -22

# =========================
# DIFICULDADE
# =========================

DIFFICULTIES = {
    "facil": {
        "initial_speed": 5,
        "speed_increment": 0.5,
        "obstacle_interval": 1800
    },
    "dificil": {
        "initial_speed": 6,
        "speed_increment": 0.7,
        "obstacle_interval": 1500
    },
    "impossivel": {
        "initial_speed": 8,
        "speed_increment": 1.0,
        "obstacle_interval": 1000
    }
}