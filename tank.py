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
<<<<<<< HEAD
        self.lifes = 2
=======
        self.lifes = 3
>>>>>>> 6a98f8d (last update)
        self.speed = 6

        self.sprites = []
        self.sprites.append(pygame.image.load('tank_up.png'))
        self.sprites.append(pygame.image.load('tank_down.png'))
        self.sprites.append(pygame.image.load('tank_left.png'))
        self.sprites.append(pygame.image.load('tank_right.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (64, 64))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

        self.direcao = direcao

<<<<<<< HEAD
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.05
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (64, 32))
=======
>>>>>>> 6a98f8d (last update)


    def move_left(self):
        self.image = self.sprites[2]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect.x -= self.speed

    def move_right(self):
        self.image = self.sprites[3]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect.x += self.speed

    def move_up(self):
        self.image = self.sprites[0]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect.y -= self.speed

    def move_down(self):
        self.image = self.sprites[1]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect.y += self.speed

    def atingido(self):
        self.lifes -= 1
    def atirar(self, tankx, tanky, dir):
        bullet = Bullet(tankx, tanky, dir)
        self.bullets.append(bullet)