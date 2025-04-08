import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")
screen.fill(WHITE)

painting = False
last_pos = None
color = BLACK
mode = "pen"  # pen, rect, circle, eraser, square, right_triangle, equilateral_triangle, rhombus
start_pos = None
eraser_size = 10

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                painting = True
                last_pos = event.pos
                start_pos = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                painting = False
                end_pos = event.pos
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = abs(x2 - x1)
                height = abs(y2 - y1)

                if mode == "rect":
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, width, height), 2)
                elif mode == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))
                    pygame.draw.circle(screen, color, start_pos, radius, 2)
                elif mode == "square":
                    side = min(width, height)
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, side, side), 2)
                elif mode == "right_triangle":
                    pygame.draw.polygon(screen, color, [(x1, y1), (x1, y2), (x2, y2)], 2)
                elif mode == "equilateral_triangle":
                    side = abs(x2 - x1)
                    height = (math.sqrt(3) / 2) * side
                    points = [(x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)]
                    pygame.draw.polygon(screen, color, points, 2)
                elif mode == "rhombus":
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    points = [(center_x, y1), (x2, center_y), (center_x, y2), (x1, center_y)]
                    pygame.draw.polygon(screen, color, points, 2)

        elif event.type == pygame.MOUSEMOTION:
            if painting:
                if mode == "pen":
                    pygame.draw.line(screen, color, last_pos, event.pos, 3)
                    last_pos = event.pos
                elif mode == "eraser":
                    pygame.draw.line(screen, WHITE, last_pos, event.pos, eraser_size)
                    last_pos = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rect"
            elif event.key == pygame.K_c:
                mode = "circle"
            elif event.key == pygame.K_p:
                mode = "pen"
            elif event.key == pygame.K_e:
                mode = "eraser"
            elif event.key == pygame.K_s:
                mode = "square"
            elif event.key == pygame.K_t:
                mode = "right_triangle"
            elif event.key == pygame.K_u:
                mode = "equilateral_triangle"
            elif event.key == pygame.K_h:
                mode = "rhombus"
            elif event.key == pygame.K_1:
                color = (255, 0, 0)  # Красный
            elif event.key == pygame.K_2:
                color = (0, 255, 0)  # Зелёный
            elif event.key == pygame.K_3:
                color = (0, 0, 255)  # Синий
            elif event.key == pygame.K_4:
                color = BLACK  # Чёрный

    pygame.display.flip()

pygame.quit()
