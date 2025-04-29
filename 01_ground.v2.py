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

# Game variables
ground = 300 # ground height
on_ground = True # telling program if lama is on the ground (default)
gravity = 0.5 # Gravity 

