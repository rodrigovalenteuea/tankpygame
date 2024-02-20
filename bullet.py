import pygame.rect


class Bullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy, dir):
        pygame.sprite.Sprite.__init__(self)


        self.color = (255, 255, 255)
        self.speedx = 5
        self.speedy = 5
        self.posx = posx
        self.posy = posy
        self.width = 20
        self.height = 20

        self.dir = dir
        self.image = pygame.image.load("square.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.topleft = self.posx, self.posy

    def create_bullet(self, screen):
        pygame.draw.rect(screen, self.color, [self.posx, self.posy, self.width, self.height])

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

    def moviment(self):
        if self.dir == 1:
            self.rect.x -= self.speedx
        elif self.dir == 2:
            self.rect.x += self.speedx
        elif self.dir == 3:
            self.rect.y -= self.speedy
        else:
            self.rect.y += self.speedy