"""Tilføj keyboard kontrol og korrekt opdatering af skærm til dette spil"""

import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

rectangle = pygame.Rect((300, 250, 50, 50))

run = True
while run:

    # Opdater skærm korrekt
    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, (255, 0, 0), rectangle)

    # Keyboard kontrol
    key = pygame.key.get_pressed()

    if key[pygame.K_UP]:
        rectangle.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        rectangle.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        rectangle.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        rectangle.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
