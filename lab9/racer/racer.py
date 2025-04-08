import pygame, sys
from pygame.locals import *
import random

pygame.init()

# Частота обновления кадров
FPS = 60
FramePerSec = pygame.time.Clock()

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Параметры экрана и дороги
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
ROAD_LEFT = 50
ROAD_RIGHT = 350
SPEED = 3
SCORE = 0
COINS = 0

# Шрифт
font = pygame.font.SysFont("Verdana", 20)

# Фон и начальная позиция фона
background = pygame.image.load(r"\Users\tursy\OneDrive\Рабочий стол\python\Python\AnimatedStreet.png")
background_y = 0

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer")

# Класс врага (машины-соперника)
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"\Users\tursy\OneDrive\Рабочий стол\python\Python\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1  # Увеличиваем счёт при прохождении врагом экрана
            self.rect.top = 0
            self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), 0)

# Класс монеты
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomize_coin()

    def randomize_coin(self):
        # Генерация размера и стоимости монеты
        if random.choice([True, False]):
            self.size = (50, 50)
            self.value = 3
        else:
            self.size = (30, 30)
            self.value = 1
        self.image = pygame.image.load(r"\Users\tursy\OneDrive\Рабочий стол\python\Python\coin.png")
        self.image = pygame.transform.scale(self.image, self.size)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(ROAD_LEFT, ROAD_RIGHT), random.randint(40, SCREEN_HEIGHT - 40))

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.respawn()

    def respawn(self):
        self.randomize_coin()

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"\Users\tursy\OneDrive\Рабочий стол\python\Python\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        # Движение игрока по нажатию клавиш
        if self.rect.left > ROAD_LEFT and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < ROAD_RIGHT and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Создание объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Столкновение с врагом = конец игры
    if pygame.sprite.spritecollideany(P1, enemies):
        game_over_font = pygame.font.SysFont("Verdana", 40)
        game_over_text = game_over_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 20))
        pygame.display.update()
        pygame.time.delay(2000)  
        pygame.quit()
        sys.exit()

    # Прокрутка фона
    background_y = (background_y + SPEED) % background.get_height()
    screen.blit(background, (0, background_y))
    screen.blit(background, (0, background_y - background.get_height()))

    # Отображение счёта и монет
    scores = font.render(f"Score: {SCORE}", True, BLACK)
    screen.blit(scores, (10, 10))

    coins_text = font.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coins_text, (300, 10))

    for enemy in enemies:
        enemy.move()

    # Отображение всех объектов
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    # Столкновение с монетой
    if pygame.sprite.spritecollideany(P1, coins):
        COINS += C1.value  # Прибавляем очки за монету
        C1.respawn()
        if COINS % 5 == 0:  # Каждые 5 монет — увеличение скорости
            SPEED += 1
            print(f"Speed increased! New SPEED: {SPEED}")

    pygame.display.update()
    FramePerSec.tick(FPS)
