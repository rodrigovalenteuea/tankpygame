import pygame.rect


class Bullet:
    def __init__(self, tankid, color, speedx, speedy, posx, posy, width, height):
        self.tankid = tankid
        self.color = color
        self.speedx = speedx
        self.speedy = speedy
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height

    def create_bullet(self, screen):
        pygame.draw.rect(screen, self.color, [self.posx, self.posy, self.width, self.height])

    def moviment_right(self):
        self.posx = self.posx + self.speedx
        return self.posx

    def moviment_left(self):
        self.posx = self.posx - self.speedx
        return self.posx

    def moviment_up(self):
        self.posy = self.posy - self.speedy
        return self.posy

    def moviment_down(self):
        self.posy = self.posy + self.speedy
        return self.posy
