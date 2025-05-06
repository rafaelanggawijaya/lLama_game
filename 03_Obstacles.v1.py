import pygame
import sys


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
WHITE = (255, 255, 255) # for background
BLACK = (0, 0, 0) # ground
LLAMA_COLOR = (200, 100, 255) # Llama
OBSTACLE_COLOR = (0, 200, 100) # obstacle 

# Game variables
ground = 300 # ground height
on_ground = True # telling program if lama is on the ground (default)
gravity = 0.5 # Gravity 
llama_velocity = 0 # variable which will be affected by gravity

# Llama (player)
llama_rect = pygame.Rect(100, ground, 50, 50)

# Obstacle
obstacle_rect = pygame.Rect(WIDTH, 300, 50, 50)

# Game state
game_active = True

# Main game loop
while True:
    # sets colour of game background
    screen.fill(WHITE)
    # quit game (helps testing)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground:
                    llama_velocity = -10
                    on_ground = False
    if game_active:
        # Llama movement
        llama_velocity += gravity
        llama_rect.y += llama_velocity
        # makes sures llama does not go through ground
        if llama_rect.bottom >= 350:
            llama_rect.bottom = 350
            on_ground = True
            llama_velocity = 0
        # Draw characters
        pygame.draw.line(screen, BLACK, (0, 350), (WIDTH, 350), 2) # ground
        pygame.draw.rect(screen, LLAMA_COLOR, llama_rect) # llama
        pygame.draw.rect(screen, OBSTACLE_COLOR, obstacle_rect) # obstacle
    # sets the colour
    pygame.display.flip()
    # Frame rate
    clock.tick(60)
        