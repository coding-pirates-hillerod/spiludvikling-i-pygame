from random import randint

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


class Alien(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./alien2.png")
        self.rect = self.image.get_rect()

        # Tilføjelse af tilfældig startposition
        self.rect.center = (randint(50, SCREE_WIDTH - 50), 100)

    def update(self) -> None:
        self.rect.y += 2

        if self.rect.top > SCREE_HEIGHT:
            self.kill()


spaceship = Spaceship()
spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship)

alien = Alien()
alien_group = pygame.sprite.Group()
alien_group.add(alien)

run = True
while run:

    clock.tick(60)

    screen.blit(bg, (0, 0))

    spaceship_group.update()
    alien_group.update()

    spaceship_group.draw(screen)
    alien_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
