import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set game constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
SPEED = 15  # Game speed (higher = faster)

# Initialize game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
direction = 'RIGHT'
change_to = direction
score = 0

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

# Fonts
SCORE_FONT = pygame.font.SysFont('timesnewroman', 25)
GAME_OVER_FONT = pygame.font.SysFont('timesnewroman', 90)

# Function to generate food in a valid position
def generate_food():
    while True:
        food = [random.randrange(1, (WIDTH//10)) * 10, random.randrange(1, (HEIGHT//10)) * 10]
        if food not in snake_body:
            return food

food_pos = generate_food()

# Function to display score
def show_score(score):
    score_text = SCORE_FONT.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Function to display game over screen
def game_over():
    screen.fill(BACKGROUND_COLOR)
    game_over_text = GAME_OVER_FONT.render('GAME OVER', True, (255, 255, 255))
    game_over_rect = game_over_text.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(game_over_text, game_over_rect)
    pygame.display.update()
    pygame.time.wait(2000)
    pygame.quit()
    sys.exit()

# Game loop
clock = pygame.time.Clock()
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Update direction
    direction = change_to

    # Move the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing
    snake_body.insert(0, list(snake_pos))
    
    # Check if food is eaten
    if snake_pos == food_pos:
        score += 1
        food_pos = generate_food()  # Generate new food
    else:
        snake_body.pop()  # Remove last segment if no food eaten

    # Check for collisions
    if (
        snake_pos[0] < 0 or snake_pos[0] >= WIDTH or
        snake_pos[1] < 0 or snake_pos[1] >= HEIGHT or
        snake_pos in snake_body[1:]
    ):
        game_over()

    # Update display
    screen.fill(BACKGROUND_COLOR)
    for segment in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], 10, 10))
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Show score
    show_score(score)

    # Refresh game screen
    pygame.display.update()
    
    # Control game speed
    clock.tick(SPEED)
