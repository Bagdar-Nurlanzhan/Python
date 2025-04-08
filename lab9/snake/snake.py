import pygame, sys, copy, random, time

pygame.init()
scale = 15

score, level, SPEED = 0, 0, 10

display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

snake_colour = (255, 137, 0)
snake_head = (255, 247, 0)
font_colour = (255, 255, 255)
defeat_colour = (255, 0, 0)
background_top = (0, 0, 50)
background_bottom = (0, 0, 0)

class Snake:
    def __init__(self, x, y):
        self.w = self.h = scale
        self.x_dir, self.y_dir = 1, 0
        self.history = [[x, y]]
        self.length = 1

    def reset(self):
        self.__init__(250 - scale, 250 - scale)

    def show(self):
        for i in range(self.length):
            color = snake_head if i == 0 else snake_colour
            pygame.draw.rect(display, color, (*self.history[i], self.w, self.h))

    def check_eaten(self, fx, fy):
        return abs(self.history[0][0] - fx) < scale and abs(self.history[0][1] - fy) < scale

    def check_level(self):
        return self.length % 5 == 0

    def grow(self):
        self.length += 1
        self.history.append(self.history[-1])

    def death(self):
        for i in range(1, self.length):
            if self.history[0] == self.history[i] and self.length > 2:
                return True

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale

class Food:
    def __init__(self):
        self.new_location()

    def new_location(self):
        self.x = random.randint(1, 33) * scale
        self.y = random.randint(1, 33) * scale
        self.color = (random.randint(50,255), random.randint(50,255), random.randint(50,255))
        self.weight = random.randint(1, 5)  
        self.timer = random.randint(80, 200)  

    def show(self):
        pygame.draw.rect(display, self.color, (self.x, self.y, scale, scale))
        self.timer -= 1
        if self.timer <= 0:
            self.new_location()  
def show_text(text, x, y, size=20, color=font_colour):
    font = pygame.font.SysFont(None, size)
    render = font.render(text, True, color)
    display.blit(render, (x, y))

def gameLoop():
    global score, level, SPEED
    snake = Snake(250, 250)
    food = Food()

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT or (e.type == pygame.KEYDOWN and e.key == pygame.K_q):
                pygame.quit(); sys.exit()
            if e.type == pygame.KEYDOWN:
                if snake.y_dir == 0:
                    if e.key == pygame.K_UP: snake.x_dir, snake.y_dir = 0, -1
                    if e.key == pygame.K_DOWN: snake.x_dir, snake.y_dir = 0, 1
                elif snake.x_dir == 0:
                    if e.key == pygame.K_LEFT: snake.x_dir, snake.y_dir = -1, 0
                    if e.key == pygame.K_RIGHT: snake.x_dir, snake.y_dir = 1, 0

        for y in range(500):
            c = [background_top[i] + (background_bottom[i] - background_top[i]) * y / 500 for i in range(3)]
            pygame.draw.line(display, c, (0, y), (500, y))

        snake.show()
        snake.update()
        food.show()
        show_text(f"Score: {score}", scale, scale)
        show_text(f"Level: {level}", 90 - scale, scale)

        if snake.check_eaten(food.x, food.y):
            score += food.weight  
            snake.grow()
            food.new_location()

        if snake.check_level():
            level += 1
            SPEED += 1
            snake.grow()
            food.new_location()

        if snake.death():
            score, level = 0, 0
            show_text("Game Over!", 50, 200, 100, defeat_colour)
            pygame.display.update()
            time.sleep(2)
            snake.reset()

        head = snake.history[0]
        if head[0] >= 500: head[0] = 0
        if head[0] < 0: head[0] = 500
        if head[1] >= 500: head[1] = 0
        if head[1] < 0: head[1] = 500

        pygame.display.update()
        clock.tick(SPEED)

gameLoop()
