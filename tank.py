import pygame
from bullet import Bullet
class Tank(pygame.sprite.Sprite):
    def __init__(self, direcao):
        pygame.sprite.Sprite.__init__(self)

        self.bullets = []
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False
        self.lifes = 2
        self.speed = 6

        self.sprites = []
        self.sprites.append(pygame.image.load('tank1.png'))
        self.sprites.append(pygame.image.load('tank2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (64, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

        self.direcao = direcao

    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (64, 32))

    def atacar(self):
        self.animar = True

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def atingido(self):
        self.lifes -= 1
    def atirar(self, tankx, tanky, dir):
        bullet = Bullet(tankx, tanky, dir)
        self.bullets.append(bullet)