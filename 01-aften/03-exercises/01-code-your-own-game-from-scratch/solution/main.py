# Step 1 - Importer og initialisering pygame
import pygame

pygame.init()


# Step 2 - Definer dit "Game Window"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Step 3 - Initialiser dit "Game Loop"
run = True
while run:

    # Step 4 - Tjek for events (her for pygames "QUIT" event)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
