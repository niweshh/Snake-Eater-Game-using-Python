import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width, height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Eater")

# Set up colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Set up the game clock
clock = pygame.time.Clock()

# Set up the snake and food
snake_head = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
food_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
food_spawned = True
direction = "RIGHT"
change_to = direction
score = 0

# Set up game over flag
game_over = False

# Game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Validate direction
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    elif change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    elif change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    elif change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

    # Update snake position
    if direction == "UP":
        snake_head[1] -= 10
    elif direction == "DOWN":
        snake_head[1] += 10
    elif direction == "LEFT":
        snake_head[0] -= 10
    elif direction == "RIGHT":
        snake_head[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_head))
    if snake_head[0] == food_position[0] and snake_head[1] == food_position[1]:
        score += 10
        food_spawned = False
    else:
        snake_body.pop()

    # Food spawn
    if not food_spawned:
        food_position = [random.randrange(1, width // 10) * 10, random.randrange(1, height // 10) * 10]
    food_spawned = True

    # Game over conditions
    if snake_head[0] < 0 or snake_head[0] > width - 10 or snake_head[1] < 0 or snake_head[1] > height - 10:
        game_over = True
    for block in snake_body[1:]:
        if block[0] == snake_head[0] and block[1] == snake_head[1]:
            game_over = True

    # Fill the window with background color
    window.fill(black)

    # Draw snake and food
    for pos in snake_body:
        pygame.draw.rect(window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, red, pygame.Rect(food_position[0], food_position[1], 10, 10))

    # Display score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, white)
    window.blit(text, [10, 10])

    # Update the game display
    pygame.display.update()

    # Set the game speed
    clock.tick(20)

# Quit the game
pygame.quit()
