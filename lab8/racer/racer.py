import pygame, sys, os
from pygame.locals import *
import random, time
pygame.init()
pygame.mixer.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
LEVEL = 1

font_big = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over_text = font_big.render("Game Over", True, BLACK)

BASE_DIR = os.path.dirname(__file__)
def load_img(name): return pygame.image.load(os.path.join(BASE_DIR, name))
def load_sound(name):
    path = os.path.join(BASE_DIR, name)
    return pygame.mixer.Sound(path) if os.path.exists(path) else None

background = load_img("AnimatedStreet.png")
player_img = load_img("Player.png")
enemy_img = load_img("Enemy.png")
crash_sound = load_sound("lab8_game_crash.wav")

DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect(center=(160, 520))

    def move(self):
        keys = pygame.key.get_pressed()
        if self.rect.left > 0 and keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))

    def move(self):
        global SCORE, LEVEL, SPEED
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
            if SCORE % 10 == 0:
                LEVEL += 1
                SPEED += 1

P1 = Player()
E1 = Enemy()

all_sprites = pygame.sprite.Group(P1, E1)
enemies = pygame.sprite.Group(E1)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.01
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    score_text = font_small.render(f"Score: {SCORE}  Level: {LEVEL}", True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    if pygame.sprite.spritecollideany(P1, enemies):
        if crash_sound:
            crash_sound.play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over_text, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
