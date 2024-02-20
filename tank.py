import pygame
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

        self.speed = 5

        self.sprites = []
        self.sprites.append(pygame.image.load('tank1.png'))
        self.sprites.append(pygame.image.load('tank2.png'))
        self.atual = 0
        self.image = self.sprites[self.atual]

        self.image = pygame.transform.scale(self.image, (64, 32))

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        self.animar = False

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

