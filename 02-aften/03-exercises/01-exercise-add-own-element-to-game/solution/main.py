"""
Hvordan man skaber sit eget spil med en rektangel tilføjet til skærmen
"""

import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

# Step 1 - Initialiser rektangel
rectangle = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    # Step 2 - Tegn rektangel på "Game Window"
    pygame.draw.rect(screen, (255, 0, 0), rectangle)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Step 3 - Opdater "Game Window"
    pygame.display.update()

pygame.quit()
