import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display window
window_width, window_height = 400, 480
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake")
font = pygame.font.Font('freesansbold.ttf', 32)
is_game_over = False

def drawGrid():

    for x in range(0, window_width, blockSize):
        for y in range(0, window_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)


GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BROWN = (101, 69, 31)
blockSize = 20

radius = 2


def create_cube(x, y):

    return pygame.Rect(x, y, 20, 20)

# x, y, width_snake, height_snake = 250, 400, 20, 20

vel = 20
x_snake, y_snake = 20, 20
snake = pygame.Rect(60, 60, x_snake, y_snake)
x_food, y_food = random.randint(0, blockSize-1)*blockSize, random.randint(0, blockSize-1)*blockSize
food = pygame.Rect(x_food, y_food, blockSize, blockSize)
snake_coordinates = []

running = True

total_snakes = []
total_snakes.append(snake)

def game_over_text():

    game_over_text = font.render(f"Game Over!", True, BROWN)
    screen.blit(game_over_text, (100, 240))

def move_snake():

    for i in range(len(total_snakes) - 1, 0, -1):
        total_snakes[i].y, total_snakes[i].x = total_snakes[i - 1].y, total_snakes[i - 1].x

def food_capture(food):

    if food.x == snake.x and food.y == snake.y:
        idx = snake_coordinates.index((total_snakes[0].x, total_snakes[0].y))
        if (food.x - snake_coordinates[idx-1][0]) > 0 and (food.y == snake_coordinates[idx-1][1]):
            total_snakes[0].x = total_snakes[0].x + vel
            total_snakes.append(create_cube(food.x-len(total_snakes)*2, food.y))
        elif (snake_coordinates[idx-1][0] - food.x) > 0 and (food.y == snake_coordinates[idx-1][1]):
            total_snakes[0].x = total_snakes[0].x - vel
            total_snakes.append(create_cube(food.x + len(total_snakes)*2, food.y))
        elif (snake_coordinates[idx - 1][0] == food.x) and (food.y - snake_coordinates[idx - 1][1]) > 0:
            total_snakes[0].y = total_snakes[0].y + vel
            total_snakes.append(create_cube(food.x, food.y - len(total_snakes)*2))
        elif (snake_coordinates[idx - 1][0] == food.x) and (snake_coordinates[idx - 1][1] - food.y) > 0:
            total_snakes[0].y = total_snakes[0].y - vel
            total_snakes.append(create_cube(food.x, food.y + len(total_snakes)*2))

        pygame.time.delay(50)
        x_food, y_food = random.randint(0, blockSize-1) * blockSize, random.randint(0, blockSize-1) * blockSize
        food = pygame.Rect(x_food, y_food, blockSize, blockSize)

    return food


while running:

    screen.fill(BLACK)
    pygame.time.delay(100)
    drawGrid()
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black color

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        move_snake()
        total_snakes[0].x = total_snakes[0].x - vel

    if keys[pygame.K_RIGHT]:
        move_snake()
        total_snakes[0].x = total_snakes[0].x + vel

    if keys[pygame.K_UP]:
        move_snake()
        total_snakes[0].y = total_snakes[0].y - vel

    if keys[pygame.K_DOWN]:
        move_snake()
        total_snakes[0].y = total_snakes[0].y + vel

    snake_coordinates.append((total_snakes[0].x, total_snakes[0].y))

    pygame.draw.rect(screen, RED, total_snakes[0])
    pygame.draw.rect(screen, GREEN, food)

    for i in range(len(total_snakes) - 1, 0, -1):
        pygame.draw.rect(screen, YELLOW, total_snakes[i])

    pygame.draw.circle(screen, BLACK, (total_snakes[0].x + 5, total_snakes[0].y + 5), radius)
    pygame.draw.circle(screen, BLACK, (total_snakes[0].x + 15, total_snakes[0].y + 5), radius)

    food = food_capture(food)

    if total_snakes[0].x >= window_width or total_snakes[0].x < 0 or total_snakes[0].y >= window_height or total_snakes[0].y < 0:
        is_game_over = True
        game_over_text()
        running = False

    pygame.display.update()

    if is_game_over:
        pygame.time.wait(5000)

pygame.quit()
