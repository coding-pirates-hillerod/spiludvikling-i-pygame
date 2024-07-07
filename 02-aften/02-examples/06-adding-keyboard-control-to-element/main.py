import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

rectangle = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    pygame.draw.rect(screen, (255, 0, 0), rectangle)

    # Step 1 - Erklær og initialiser variabel for tjek af handling

    # Step 2 - Tjek for handling med "if statements"

    # Step 3 - Foretag ændring af element for hvert tjek

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
