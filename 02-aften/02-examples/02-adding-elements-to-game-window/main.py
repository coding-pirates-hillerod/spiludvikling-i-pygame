import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

# Step 1 - Tilføj dit element her (før dit "Game Loop")

run = True
while run:

    # Step 2 - Tegn dit element på dit "Game Window" her

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Step 3 - Opdater dit "Game Window", så elementet tegnes

pygame.quit()
