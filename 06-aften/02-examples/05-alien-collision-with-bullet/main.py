from random import randint

import pygame

pygame.init()

SCREE_WIDTH = 600
SCREE_HEIGHT = 800

screen = pygame.display.set_mode((SCREE_WIDTH, SCREE_HEIGHT))

clock = pygame.time.Clock()

last_alien = pygame.time.get_ticks()
alien_cooldown = 1500
game_over = False

bg = pygame.image.load("./bg.png")


class Spaceship(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = (300, 750)
        self.last_shot = pygame.time.get_ticks()

    def update(self) -> None:
        global game_over
        bullet_cooldown = 250

        if not game_over:
            key = pygame.key.get_pressed()

            if key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.left -= 5
            if key[pygame.K_RIGHT] and self.rect.right < SCREE_WIDTH:
                self.rect.left += 5

            time_now = pygame.time.get_ticks()
            if key[pygame.K_SPACE] and time_now - self.last_shot > bullet_cooldown:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                bullet_group.add(bullet)
                self.last_shot = time_now

        if pygame.sprite.spritecollide(self, alien_group, False):
            game_over = True


class Alien(pygame.sprite.Sprite):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./alien2.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(50, SCREE_WIDTH - 50), 100)

    def update(self) -> None:
        global game_over

        if not game_over:
            self.rect.y += 2

            if self.rect.top > SCREE_HEIGHT:
                self.kill()

        # Tjek for "Alien" kollision med "Bullet"
        if pygame.sprite.spritecollide(self, bullet_group, True):
            self.kill()


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        self.rect.y -= 5


spaceship = Spaceship()
spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship)

alien = Alien()
alien_group = pygame.sprite.Group()
alien_group.add(alien)

bullet_group = pygame.sprite.Group()

run = True
while run:

    clock.tick(60)

    screen.blit(bg, (0, 0))

    if not game_over:
        time_now = pygame.time.get_ticks()
        if time_now - last_alien > alien_cooldown:
            new_alien = Alien()
            alien_group.add(new_alien)
            last_alien = time_now

    spaceship_group.update()
    alien_group.update()
    bullet_group.update()

    spaceship_group.draw(screen)
    alien_group.draw(screen)
    bullet_group.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
