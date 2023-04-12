import pygame
import time
import random

pygame.init()

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)

# Set the dimensions of the game window
DIS_WIDTH = 600
DIS_HEIGHT = 400

# Create the game window and set its title
DIS = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption('Snake Game')

# Set the frame rate and block size
SNAKE_BLOCK = 10
SNAKE_SPEED = 15

# Set up fonts for displaying text
FONT_STYLE = pygame.font.SysFont("comicsansms", 30)
SCORE_FONT = pygame.font.SysFont("comicsansms", 35)


def draw_score(score):
    value = SCORE_FONT.render("Score: " + str(score), True, WHITE)
    DIS.blit(value, [DIS_WIDTH - value.get_width() - 10, 10])


def draw_snake(snake_block, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(DIS, GREEN, [x, y, snake_block, snake_block])


def draw_message(msg, color):
    mesg = FONT_STYLE.render(msg, True, color)
    x = (DIS_WIDTH - mesg.get_width()) / 2
    y = (DIS_HEIGHT - mesg.get_height()) / 2
    DIS.blit(mesg, [x, y])


def game_loop():
    game_over = False
    game_close = False

    # Set the starting position of the snake
    x = DIS_WIDTH / 2
    y = DIS_HEIGHT / 2
    x_change = 0
    y_change = 0

    # Initialize the snake list and length
    snake_list = []
    snake_length = 1

    # Set the initial position of the food
    food_x = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
    food_y = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0

    while not game_over:

        while game_close:
            DIS.fill(BLACK)
            draw_message("Game over! Press C to play again or Q to quit", RED)
            draw_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = SNAKE_BLOCK
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -SNAKE_BLOCK
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = SNAKE_BLOCK
                    x_change = 0

        # Update the position of the snake
        x += x_change
        y += y_change

        # Check if the snake has collided with the walls of the game window
        if x >= DIS_WIDTH or x < 0 or y >= DIS_HEIGHT or y < 0:
            game_close = True

        # Update the position of the food and increase the length of the snake if it has eaten the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, DIS_WIDTH - SNAKE_BLOCK) / 10.0) * 10.0
            food_y = round(random.randrange(0, DIS_HEIGHT - SNAKE_BLOCK) / 10.0) * 10.0
            snake_length += 1

        # Draw the game window
        DIS.fill(BLACK)
        pygame.draw.rect(DIS, RED, [food_x, food_y, SNAKE_BLOCK, SNAKE_BLOCK])

        # Update the snake list and draw the snake
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        draw_score(snake_length - 1)
        pygame.display.update()

        # Set the game frame rate
        clock = pygame.time.Clock()
        clock.tick(SNAKE_SPEED)

    # Quit pygame and the program
    pygame.quit()
    quit()
game_loop()