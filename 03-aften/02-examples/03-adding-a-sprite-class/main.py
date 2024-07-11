import pygame
from pygame.sprite import _Group

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))


# Step 1 - Klasse til din Sprite - her et "Spaceship"
class Spaceship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [400, 550]


# Step 2 - Initialiser Sprite og Sprite Group

# Step 3 - Tilføj Sprite til Sprite Group

run = True
while run:

    screen.fill((0, 0, 0))

    # Step 4 - kald "draw" metoden på din Sprite gruppe

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
