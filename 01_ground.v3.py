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

# Colours
WHITE = (255, 255, 255) # background
BLACK = (0, 0, 0) # ground


# Game variables
ground = 300 # ground height
on_ground = True # telling program if lama is on the ground (default)
gravity = 0.5 # Gravity 

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
        # Draw characters
        pygame.draw.line(screen, BLACK, (0, 350), (WIDTH, 350), 2) # ground
    
    # sets the colour
    pygame.display.flip()