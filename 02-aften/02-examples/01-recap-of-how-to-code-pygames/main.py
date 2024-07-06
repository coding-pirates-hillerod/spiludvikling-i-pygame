"""Koding af spil i Pygame foregår som udgangspunkt via følgende 4 steps"""

# Step 1 - Import og initialering af Pygame
import pygame

pygame.init()

# Step 2 - Definition af ens "Game Window"
SCREE_WIDTH = 800
SCREE_HEIGHT = 600

# Step 3 - Afvikling af "Game Loop"
run = True
while run:

    # Step 4 - Tjek for events i ens "Event Handler"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
