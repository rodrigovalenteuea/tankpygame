import pygame.rect


class Bullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy, dir):
        pygame.sprite.Sprite.__init__(self)


<<<<<<< HEAD
        self.color = (255, 255, 255)
        self.speedx = 5
        self.speedy = 5
=======


        self.color = (255, 255, 255)
        self.speedx = 10
        self.speedy = 10
>>>>>>> 6a98f8d (last update)
        self.posx = posx
        self.posy = posy
        self.width = 20
        self.height = 20
<<<<<<< HEAD

        self.dir = dir
        self.image = pygame.image.load("square.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.posx, self.posy
=======
>>>>>>> 6a98f8d (last update)

        self.dir = dir
        self.image = pygame.image.load("square.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.posx, self.posy

<<<<<<< HEAD
    def moviment_right(self):
        self.rect.x += self.speedx

    def moviment_left(self):
        self.posx = self.posx - self.speedx
        return self.posx

    def moviment_up(self):
        self.posy = self.posy - self.speedy
        return self.posy

    def moviment_down(self):
        self.posy = self.posy + self.speedy
        return self.posy

=======
>>>>>>> 6a98f8d (last update)
    def moviment(self):
        if self.dir == 1:
            self.rect.x -= self.speedx
        elif self.dir == 2:
            self.rect.x += self.speedx
        elif self.dir == 3:
            self.rect.y -= self.speedy
        else:
            self.rect.y += self.speedy