import pygame
import sys
import random

# functions

# loading previous high score
def load_high_score():
    try:
        hi_score_file = open("Hi_score.txt", "r")
    except IOError:
        hi_score_file = open("Hi_score.txt", 'w')
        hi_score_file.write("0")
    hi_score_file = open("Hi_score.txt", "r")
    value = hi_score_file.read()
    hi_score_file.close()
    return value

# updating the high score
def update_high_score(score, high_score):
    if int(score) > int(high_score):
        return score
    else:
        return high_score

# saving high scores
def save_high_score(high_score):
    high_score_file = open("Hi_score.txt", 'w')
    high_score_file.write(str(high_score))
    high_score_file.close()

# Starting pygame
pygame.init()

# Setting up screen dimensions
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Llama Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game variables
ground = 300
on_ground = True
gravity = 0.5
llama_velocity = 0
score = 0
start_time = pygame.time.get_ticks()

# High score variable
high_score = load_high_score()

# Load llama images and scale them
llama_images = [
    pygame.image.load("assets/Llama.png"),
    pygame.image.load("assets/Llama2.png"),
    pygame.image.load("assets/Llama3.png")
]
llama_images = [pygame.transform.scale(img, (50, 50)) for img in llama_images]
llama_index = 0
llama_animation_timer = 0

# Load cactus image and scale it
cactus_image = pygame.image.load("assets/cactus.png")
cactus_image = pygame.transform.scale(cactus_image, (50, 50))

# Llama (player)
llama_rect = pygame.Rect(70, ground, 50, 50)

# Obstacle
obstacle_rect = pygame.Rect(WIDTH, 300, 50, 50)

# Game state
game_active = True

# Main game loop
while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(high_score)
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    llama_velocity = -10
                    on_ground = False
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                high_score = update_high_score(score, high_score)
                save_high_score(high_score)
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

        # Hitboxes
        llama_hitbox = pygame.Rect(llama_rect.x + 5, llama_rect.y + 5, 40, 40)
        cactus_hitbox = pygame.Rect(obstacle_rect.x + 5, obstacle_rect.y + 5, 40, 40)

        # Collision detection using hitboxes
        if llama_hitbox.colliderect(cactus_hitbox):
            game_active = False

        # Score
        score = (pygame.time.get_ticks() - start_time) // 1000
        score_surface = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_surface, (10, 10))

        # Animate llama
        llama_animation_timer += 1
        if llama_animation_timer >= 10:
            llama_index = (llama_index + 1) % len(llama_images)
            llama_animation_timer = 0

        # Draw ground
        pygame.draw.line(screen, BLACK, (0, 350), (WIDTH, 350), 2)

        # Draw llama and cactus
        screen.blit(llama_images[llama_index], llama_rect)
        screen.blit(cactus_image, obstacle_rect)

        # Draw hitboxes (for debugging)
        pygame.draw.rect(screen, (255, 0, 0), llama_hitbox, 2)
        pygame.draw.rect(screen, (255, 0, 0), cactus_hitbox, 2)

    else:
        game_over_text = font.render("Game Over! Press R to restart", True, BLACK)
        screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2))
        high_score_surface = font.render(f"High Score: {high_score}", True, BLACK)
        screen.blit(high_score_surface, (WIDTH // 2 - 80, HEIGHT // 2 + 40))

    pygame.display.flip()
    clock.tick(60)
