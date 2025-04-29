import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Llama Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LLAMA_COLOR = (200, 100, 255)
OBSTACLE_COLOR = (0, 200, 100)

# Game variables
gravity = 0.5
llama_y = 300
llama_velocity = 0
on_ground = True
score = 0
start_time = pygame.time.get_ticks()

# Llama (player)
llama_rect = pygame.Rect(100, llama_y, 50, 50)

# Obstacle
obstacle_rect = pygame.Rect(WIDTH, 300, 50, 50)

# Game state
game_active = True

# Main game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    llama_velocity = -10
                    on_ground = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                # Reset game
                game_active = True
                llama_rect.y = 300
                llama_velocity = 0
                on_ground = True
                obstacle_rect.x = WIDTH
                start_time = pygame.time.get_ticks()

    if game_active:
        # Llama movement
        llama_velocity += gravity
        llama_rect.y += llama_velocity
        if llama_rect.bottom >= 350:
            llama_rect.bottom = 350
            on_ground = True
            llama_velocity = 0

        # Obstacle movement
        obstacle_rect.x -= 5
        if obstacle_rect.right < 0:
            obstacle_rect.left = WIDTH + random.randint(300, 600)

        # Collision detection
        if llama_rect.colliderect(obstacle_rect):
            game_active = False

        # Score
        score = (pygame.time.get_ticks() - start_time) // 1000
        score_surface = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (10, 10))

        # Draw characters
        pygame.draw.rect(screen, LLAMA_COLOR, llama_rect)
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle_rect)
        pygame.draw.line(screen, BLACK, (0, 350), (WIDTH, 350), 2)

    else:
        game_over_text = font.render("Game Over! Press R to restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))

    pygame.display.flip()
    clock.tick(60)