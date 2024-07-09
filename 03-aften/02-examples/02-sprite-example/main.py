import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))


# Step 1 - lav en Python klasse, som nedarver fra pygame.sprite.Sprite
class SpaceShip(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]


# Step 2 - Initialiser din Sprite
spaceship = SpaceShip()

run = True
while run:
    spaceship.update()

    # Opdater "Game Window" korrekt
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(spaceship)

    pygame.display.update()

pygame.quit()
