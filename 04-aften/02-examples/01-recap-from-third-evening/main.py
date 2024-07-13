import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))


# Tilføjelse af Sprite klasse - her en "Spaceship" Sprite
class Spaceship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

    # Metode til opdatering af Sprite
    def update(self) -> None:
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.left -= 2
        if key[pygame.K_RIGHT]:
            self.rect.left += 2


# Erklæring initialisering af Sprite og Sprite Group
spaceship = Spaceship()
spaceship_group = pygame.sprite.Group()

# Tilføjelse af Sprite til Sprite Group
spaceship_group.add(spaceship)

run = True
while run:

    screen.fill((0, 0, 0))

    # Opdatering af Sprites
    spaceship_group.update()

    # Tegne Sprites på skærmen
    spaceship_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
