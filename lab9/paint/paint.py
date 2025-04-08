import pygame
import math  

pygame.init()  # Инициализация всех модулей pygame

# Размеры окна
WIDTH, HEIGHT = 800, 600

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Создаём окно и задаём заголовок
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint Application")

# Заливаем фон белым
screen.fill(WHITE)

# Переменные для рисования
painting = False           # Активно ли рисование (нажата ли мышь)
last_pos = None            # Последняя позиция мыши
color = BLACK              
mode = "pen"               
start_pos = None           
eraser_size = 10           

# Основной цикл программы
running = True
while running:
    for event in pygame.event.get():  # Обрабатываем события
        if event.type == pygame.QUIT:  # Закрытие окна
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:  # Нажатие кнопки мыши
            if event.button == 1:  # Левая кнопка
                painting = True
                last_pos = event.pos      
                start_pos = event.pos      

        elif event.type == pygame.MOUSEBUTTONUP:  # Отпускание кнопки мыши
            if event.button == 1:
                painting = False
                end_pos = event.pos       
                x1, y1 = start_pos
                x2, y2 = end_pos
                width = abs(x2 - x1)      # Ширина фигуры
                height = abs(y2 - y1)     # Высота фигуры

                
                if mode == "rect":
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, width, height), 2)
                elif mode == "circle":
                    radius = int(math.hypot(x2 - x1, y2 - y1))  # Радиус по расстоянию между точками
                    pygame.draw.circle(screen, color, start_pos, radius, 2)
                elif mode == "square":
                    side = min(width, height)  # Сторона квадрата — минимальное из ширины/высоты
                    pygame.draw.rect(screen, color, pygame.Rect(x1, y1, side, side), 2)
                elif mode == "right_triangle":
                    # Прямоугольный треугольник по 3 точкам
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

        elif event.type == pygame.KEYDOWN:  # Обработка клавиш
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
                color = BLACK       # Чёрный

    pygame.display.flip()  # Обновляем экран

pygame.quit()  # Завершение программы
