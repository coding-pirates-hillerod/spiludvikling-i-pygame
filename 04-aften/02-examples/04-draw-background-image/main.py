import pygame

pygame.init()

SCREE_WIDTH = 800
SCREE_HEIGHT = 600

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

# Step 1 - load baggrundsbillede
bg = pygame.image.load("./bg.png")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (400, 550)

    def update(self) -> None:
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.rect.left -= 2
        if key[pygame.K_RIGHT]:
            self.rect.left += 2


spaceship = Spaceship()
spaceship_group = pygame.sprite.Group()

spaceship_group.add(spaceship)

run = True
while run:

    # Step 2 - udskift "fill" metoden med "blit" metoden
    screen.blit(bg, (0, 0))

    spaceship_group.update()

    spaceship_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
