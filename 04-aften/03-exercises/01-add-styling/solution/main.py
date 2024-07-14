"""
Tilføj følgende til dette spil:

  - 1) Pænere baggrundsbillede (brug 'bg.png' i roden af mappen)

  - 2) Kontrol af "Spaceship" navigation

  - 3) Kontrol af "frame rates"
"""

import pygame

pygame.init()

SCREE_WIDTH = 600
SCREE_HEIGHT = 800

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

clock = pygame.time.Clock()

bg = pygame.image.load("./bg.png")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 750)

    def update(self) -> None:
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.left -= 5

        if key[pygame.K_RIGHT] and self.rect.right < SCREE_WIDTH:
            self.rect.left += 5


spaceship = Spaceship()
spaceship_group = pygame.sprite.Group()

spaceship_group.add(spaceship)

run = True
while run:

    clock.tick(60)

    screen.blit(bg, (0, 0))

    spaceship_group.update()

    spaceship_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
