import pygame
pygame.init()
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Movement Game")

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_speed = 20
running = True
while running:
    screen.fill((255, 255, 255)) 
    pygame.draw.circle(screen, (255, 0, 0), (ball_x, ball_y), ball_radius) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y = max(ball_radius, ball_y - ball_speed)
    if keys[pygame.K_DOWN]:
        ball_y = min(HEIGHT - ball_radius, ball_y + ball_speed)
    if keys[pygame.K_LEFT]:
        ball_x = max(ball_radius, ball_x - ball_speed)
    if keys[pygame.K_RIGHT]:
        ball_x = min(WIDTH - ball_radius, ball_x + ball_speed)
    pygame.display.flip()
    pygame.time.delay(50) 
pygame.quit()
